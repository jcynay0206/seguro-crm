from fastapi import APIRouter, Request
from backend.services.firebase import db

router = APIRouter(prefix="/api/calendly", tags=["Calendly"])

@router.post("/webhook")
async def calendly_webhook(request: Request):
    payload = await request.json()

    event = payload.get("event")
    data = payload.get("payload", {})

    invitee = data.get("invitee", {})
    event_info = data.get("event", {})

    lead = {
        "name": invitee.get("name"),
        "email": invitee.get("email"),
        "phone": "",
        "source": "calendly",
        "meta": "Agendó consulta",
        "appointment_time": event_info.get("start_time")
    }

    db.collection("leads").add(lead)

    return {"status": "ok"}
