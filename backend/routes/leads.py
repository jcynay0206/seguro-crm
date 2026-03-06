from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.firebase import save_lead, get_leads, update_lead

router = APIRouter()

# -----------------------------
# MODELOS
# -----------------------------

class LeadCreate(BaseModel):
    name: str
    email: str
    phone: str
    meta: str | None = None
    status: str = "nuevo"
    source: str = "manual"

class LeadUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    meta: str | None = None
    status: str | None = None
    source: str | None = None

# -----------------------------
# ENDPOINTS
# -----------------------------

@router.post("/create")
def create_lead(data: LeadCreate):
    save_lead(data.dict())
    return {"status": "ok"}

@router.get("/all")
def list_leads():
    return get_leads()

@router.put("/{lead_id}")
def edit_lead(lead_id: str, data: LeadUpdate):
    update_lead(lead_id, data.dict(exclude_none=True))
    return {"status": "updated"}
