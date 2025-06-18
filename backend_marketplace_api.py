from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from modules.marketplace import DrillPack
from modules.db import SessionLocal, Base, engine
import shutil, uuid, os

# Ensure DB tables exist
Base.metadata.create_all(bind=engine)

app = FastAPI()
os.makedirs('storage/drill_packs', exist_ok=True)
app.mount("/storage", StaticFiles(directory="storage"), name="storage")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/marketplace/upload")
async def upload_pack(
    coach_id: int = Form(...),
    title: str = Form(...),
    description: str = Form(""),
    price_cents: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        ext = os.path.splitext(file.filename)[1]
        fname = f"{uuid.uuid4()}{ext}"
        path = os.path.join("storage/drill_packs", fname)
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        file_url = f"/storage/drill_packs/{fname}"

        pack = DrillPack(
            coach_id=coach_id,
            title=title,
            description=description,
            price_cents=price_cents,
            file_url=file_url
        )
        db.add(pack)
        db.commit()
        db.refresh(pack)
        return {"drill_pack": {"id": pack.id, "file_url": file_url}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/marketplace/list")
def list_packs(db: Session = Depends(get_db)):
    packs = db.query(DrillPack).all()
    return [
        {
            "id": p.id,
            "coach_id": p.coach_id,
            "title": p.title,
            "file_url": p.file_url,
            "price_cents": p.price_cents,
            "commission_amount": int(p.price_cents * (p.commission_pct / 100))
        }
        for p in packs
    ]
