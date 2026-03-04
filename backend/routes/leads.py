from fastapi import APIRouter
from services.firebase import save_lead, get_leads, update_lead

router = APIRouter()

@router.post("/create")
def create_lead(data: dict):
    save_lead(data)
    return {"status": "ok"}

@router.get("/all")
def list_leads():
    return get_leads()

@router.put("/{lead_id}")
def edit_lead(lead_id: str, data: dict):
    update_lead(lead_id, data)
    return {"status": "updated"}
