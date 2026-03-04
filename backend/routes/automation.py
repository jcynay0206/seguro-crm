from fastapi import APIRouter

router = APIRouter()

@router.post("/run")
def run_automation(data: dict):
    # Aquí conectas tu lógica de automatización
    return {"status": "automation triggered"}
