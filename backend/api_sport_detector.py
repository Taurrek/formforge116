from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5178"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict_sport_enhanced/")
async def predict_sport_enhanced(file: UploadFile = File(...)):
    # Your existing prediction logic here
    contents = await file.read()
    # Dummy response for example
    return {"predicted_sport": "soccer", "confidence": 0.95, "explanation": [0.5, 0.3, 0.2]}
