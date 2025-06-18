import json
import os
import torch
from datetime import datetime
from PIL import Image
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt
from torch.cuda.amp import GradScaler, autocast  # Mixed Precision
import logging
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score
from torch.utils.tensorboard import SummaryWriter  # TensorBoard
class EarlyStopping:
    def __init__(self, patience=5, delta=0):
        self.patience = patience
        self.delta = delta
        self.best_loss = float('inf')
        self.counter = 0

    def early_stop(self, val_loss):
        if val_loss < self.best_loss - self.delta:
            self.best_loss = val_loss
            self.counter = 0                   
        else:
            self.counter += 1                 

        if self.counter >= self.patience:
            return True                             
        return False

# Set up logging and tensorboard
logging.basicConfig(filename='cross_sport_transfer.log', level=logging.INFO, format='%(asctime)s - %(message)s')
writer = SummaryWriter(log_dir='runs/cross_sport_transfer')  # TensorBoard

# Enhanced Data Augmentation
data_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.Resize(256),
    transforms.RandomCrop(224),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
    transforms.RandomAffine(degrees=15, scale=(0.8, 1.2)),
    transforms.RandomVerticalFlip(),  # Added vertical flip for more diversity
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Custom Dataset for Loading Sports Data
class SportsDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        self.data = []
        self.labels = []
        self.class_to_idx = {}

        for idx, label_folder in enumerate(os.listdir(data_dir)):
            label_folder_path = os.path.join(data_dir, label_folder)
            if os.path.isdir(label_folder_path):
                self.class_to_idx[label_folder] = idx
                for filename in os.listdir(label_folder_path):
                    file_path = os.path.join(label_folder_path, filename)
                    if file_path.endswith(('.jpg', '.png')):
                        self.data.append(file_path)
                        self.labels.append(label_folder)

        if len(self.data) == 0:
            raise ValueError(f"No images found in {data_dir}")
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        image_path = self.data[idx]
        label_name = self.labels[idx]
        label = self.class_to_idx[label_name]
        image = Image.open(image_path).convert('RGB')
        
        if self.transform:
            image = self.transform(image)
        
        return image, torch.tensor(label, dtype=torch.long)

# Load Pretrained Model and Modify for Transfer Learning
def load_pretrained_model(num_classes):
    model = models.resnet18(weights='IMAGENET1K_V1')
    
    for param in model.parameters():
        param.requires_grad = False
    
    # Adding Batch Normalization for better training stability
    model.fc = nn.Sequential(
        nn.Linear(model.fc.in_features, 512),
        nn.ReLU(),
        nn.BatchNorm1d(512),  # Batch Normalization Layer
        nn.Dropout(0.5),
        nn.Linear(512, num_classes)
    )
    return model

# Learning Rate Scheduler
def adjust_learning_rate(optimizer, epoch, lr_schedule):
    if epoch in lr_schedule:
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr_schedule[epoch]

# Save the model checkpoint
def save_checkpoint(model, epoch, optimizer, filename="model_checkpoint.pth"):
    checkpoint = {
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
    }
    torch.save(checkpoint, filename)
    print(f"Checkpoint saved at epoch {epoch}.")

# Mixed Precision Training
def fine_tune_model(model, train_loader, val_loader, optimizer, criterion, epochs=10, lr_schedule=None):
    scaler = GradScaler()
    early_stopping = EarlyStopping(patience=3)
    
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for inputs, labels in train_loader:
            optimizer.zero_grad()
            with autocast():  # Automatic Mixed Precision
                outputs = model(inputs)
                loss = criterion(outputs, labels)
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
            running_loss += loss.item()

        print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss / len(train_loader)}")
        writer.add_scalar('Training Loss', running_loss / len(train_loader), epoch)

        # Unfreeze layers after 5 epochs
        if epoch >= 5:
            for param in model.layer3.parameters():
                param.requires_grad = True
            for param in model.layer4.parameters():
                param.requires_grad = True

        # Learning rate adjustment
        if lr_schedule:
            adjust_learning_rate(optimizer, epoch, lr_schedule)

        model.eval()
        correct = 0
        total = 0
        all_preds = []
        all_labels = []
        with torch.no_grad():
            for inputs, labels in val_loader:
                outputs = model(inputs)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()
                all_preds.extend(predicted.cpu().numpy())
                all_labels.extend(labels.cpu().numpy())

        print(f"Validation Accuracy: {100 * correct / total}%")
        writer.add_scalar('Validation Accuracy', 100 * correct / total, epoch)

        if early_stopping.early_stop(running_loss):
            print("Early stopping triggered.")
            break

        save_checkpoint(model, epoch, optimizer)

        # Confusion Matrix
        cm = confusion_matrix(all_labels, all_preds)
        plt.figure(figsize=(6,6))
        plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        plt.title(f"Epoch {epoch+1} Confusion Matrix")
        plt.colorbar()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')
        plt.show()

        # Advanced Metrics
        precision = precision_score(all_labels, all_preds, average='weighted', zero_division=1)
        recall = recall_score(all_labels, all_preds, average='weighted', zero_division=1)
        f1 = f1_score(all_labels, all_preds, average='weighted')
        auc_roc = roc_auc_score(all_labels, all_preds, multi_class='ovr', average='weighted', zero_division=1)

        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"F1-Score: {f1}")
        print(f"AUC-ROC: {auc_roc}")

# Model Versioning and Metadata Saving
def save_model_metadata(model, epoch, accuracy, model_path="model_registry.json"):
    metadata = {
        "model_version": f"v{epoch}",
        "accuracy": accuracy,
        "training_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "model_description": "ResNet-18 fine-tuned on cross-sport data",
        "license": "MIT License (for model weights)",
        "model_path": model_path
    }
    
    if os.path.exists(model_path):
        with open(model_path, 'r') as f:
            registry = json.load(f)
    else:
        registry = []

    registry.append(metadata)
    
    with open(model_path, 'w') as f:
        json.dump(registry, f, indent=4)
    
    print(f"Model metadata saved to {model_path}")

# Save Model Weights with Metadata
def save_model_with_metadata(model, model_path="fine_tuned_model.pth", metadata=None):
    torch.save({
        'model_state_dict': model.state_dict(),
        'metadata': metadata
    }, model_path)
    print(f"Model and metadata saved to {model_path}")

# Main Function to Run Transfer Learning
def run_cross_sport_transfer(data_dir_source, data_dir_target, num_classes, batch_size=32, epochs=50):
    train_dataset = SportsDataset(data_dir_source, transform=data_transforms)
    val_dataset = SportsDataset(data_dir_target, transform=data_transforms)
    
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

    model = load_pretrained_model(num_classes)
    optimizer = optim.Adam(model.fc.parameters(), lr=1e-6, weight_decay=1e-5)  # Lower learning rate
    criterion = nn.CrossEntropyLoss()

    fine_tune_model(model, train_loader, val_loader, optimizer, criterion, epochs=epochs, lr_schedule={5: 1e-5, 8: 1e-6})

    model_metadata = {
        "model_version": "v1.0",
        "trained_on": "Soccer -> Basketball",
        "hyperparameters": {"lr": 1e-6, "epochs": 50},
        "license": "MIT",
        "description": "Fine-tuned ResNet-18 for cross-sport transfer learning"
    }

    save_model_with_metadata(model, metadata=model_metadata)

if __name__ == "__main__":
    data_dir_source = "/home/cj2k4211/data/soccer_data"
    data_dir_target = "/home/cj2k4211/data/basketball_data"
    num_classes = 10
    run_cross_sport_transfer(data_dir_source, data_dir_target, num_classes)

# Early Stopping Implementation
class EarlyStopping:
    def __init__(self, patience=5, delta=0):
        self.patience = patience
        self.delta = delta
        self.best_loss = float('inf')
        self.counter = 0

    def early_stop(self, val_loss):
        if val_loss < self.best_loss - self.delta:
            self.best_loss = val_loss
            self.counter = 0
        else:
            self.counter += 1

        if self.counter >= self.patience:
            return True
        return False

