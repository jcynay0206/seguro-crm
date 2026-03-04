from fastapi import APIRouter

router = APIRouter()

@router.post("/send")
def send_alert(data: dict):
    # Aquí conectas tu lógica de alertas
    return {"status": "alert sent"}
