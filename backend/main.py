from fastapi import FastAPI, Request
from backend.routes.leads import router as leads_router
from backend.routes.automation import router as automation_router
from backend.routes.alerts import router as alerts_router
from backend.routes.bot import router as bot_router

from datetime import datetime
import uuid

# IMPORTA TU DB DE FIREBASE (ajusta la ruta si tu archivo está en otro lugar)
from backend.config.firebase import db

app = FastAPI()

# ROUTERS PRINCIPALES
app.include_router(leads_router, prefix="/api/leads")
app.include_router(automation_router, prefix="/api/automation")
app.include_router(alerts_router, prefix="/api/alerts")
app.include_router(bot_router, prefix="/api/bot")

@app.get("/")
def root():
    return {"status": "backend running"}


# 🔥 ENDPOINT ESPECIAL PARA STATICFORMS
@app.post("/api/leads/staticforms")
async def staticforms_webhook(request: Request):
    data = await request.form()

    lead = {
        "id": str(uuid.uuid4()),
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "meta": data.get("meta"),
        "created_at": datetime.utcnow().isoformat(),
        "status": "nuevo",
        "source": "staticforms"
    }

    db.collection("leads").document(lead["id"]).set(lead)

    return {"success": True, "lead": lead}
