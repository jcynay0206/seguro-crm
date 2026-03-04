from fastapi import APIRouter

router = APIRouter()

@router.post("/message")
def bot_message(data: dict):
    # Aquí conectas tu lógica del bot
    return {"reply": "Mensaje recibido"}
