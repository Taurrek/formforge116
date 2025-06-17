from fastapi import FastAPI

app = FastAPI()

@app.post("/api/self-service/sdk")
async def create_sdk_session():
    return {"message": "SDK session created"}

@app.get("/api/self-service/data")
async def get_sdk_data():
    return {"data": "SDK data"}
