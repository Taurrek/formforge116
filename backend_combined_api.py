from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend_marketplace_api import app as marketplace_app

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/marketplace", marketplace_app)

@app.get("/")
def root():
    return {"status": "combined api active"}
