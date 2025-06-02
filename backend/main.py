from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for local frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict_sport_enhanced/")
async def predict_sport_enhanced(file: UploadFile = File(...)):
    # Just read the file but do nothing for now
    content = await file.read()
    # For debugging:
    print(f"Received file: {file.filename}, size: {len(content)} bytes")
    # Return dummy response
    return {
        "predicted_sport": "soccer",
        "confidence": 0.95,
        "explanation": [0.3, 0.4, 0.3]
    }
