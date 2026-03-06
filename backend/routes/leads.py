from fastapi import APIRouter, Request
from backend.services.firebase import save_lead, get_leads, update_lead

router = APIRouter()

@router.post("/create")
async def create_lead(request: Request):
    data = await request.json()
    save_lead(data)
    return {"status": "ok"}

@router.get("/all")
def list_leads():
    return get_leads()

@router.put("/{lead_id}")
async def edit_lead(lead_id: str, request: Request):
    data = await request.json()
    update_lead(lead_id, data)
    return {"status": "updated"}
