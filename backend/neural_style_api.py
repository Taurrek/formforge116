from fastapi import FastAPI, File, UploadFile
from neural_style_imitator import NeuralStyleImitator
import shutil
import os

app = FastAPI()

style_imitator = NeuralStyleImitator()

@app.post("/api/neural_style_imitate")
async def neural_style_imitate(content_image: UploadFile = File(...), style_image: UploadFile = File(...)):
    # Save uploaded images
    content_image_path = "/home/cj2k4211/formforge/uploads/content_image.jpg"
    style_image_path = "/home/cj2k4211/formforge/uploads/style_image.jpg"

    with open(content_image_path, "wb") as f:
        shutil.copyfileobj(content_image.file, f)
    
    with open(style_image_path, "wb") as f:
        shutil.copyfileobj(style_image.file, f)

    # Generate style imitation
    imitation_image = style_imitator.generate_style_imitations(content_image_path, style_image_path, iterations=100)

    # Save the output image
    output_image_path = "/home/cj2k4211/formforge/uploads/imitation_image.jpg"
    shutil.imsave(output_image_path, imitation_image)

    return {"message": "Style imitation generated successfully.", "imitation_image_path": output_image_path}
