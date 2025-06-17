import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/stream/fatigue")
def get_fatigue_data():
    # Simulate streaming fatigue data
    fatigue_data = {
        "timestamp": time.time(),
        "fatigue_level": 0.5  # Replace with actual fatigue detection logic
    }
    return JSONResponse(content=fatigue_data)
