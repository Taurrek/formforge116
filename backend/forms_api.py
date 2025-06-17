from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/forms", tags=["forms"])

# In-memory stubbed data
_forms = [
    {"id": 1, "title": "Sample Form", "description": "This is a test form."}
]

@router.get("/")
def list_forms():
    return _forms

@router.get("/{form_id}")
def get_form(form_id: int):
    for f in _forms:
        if f["id"] == form_id:
            return f
    raise HTTPException(status_code=404, detail="Form not found")
