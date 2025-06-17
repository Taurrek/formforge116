from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

marketplace_items = []

@app.get("/marketplace/list")
def get_marketplace_items():
    return marketplace_items

@app.post("/marketplace/upload")
def upload_item(item: dict):
    marketplace_items.append(item)
    return {"status": "uploaded"}
