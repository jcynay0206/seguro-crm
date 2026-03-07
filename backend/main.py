from fastapi import FastAPI, Request
from backend.routes.leads import router as leads_router
from backend.routes.automation import router as automation_router
from backend.routes.alerts import router as alerts_router
from backend.routes.bot import router as bot_router

from datetime import datetime
import uuid

# IMPORT CORRECTO DE FIREBASE
from backend.services.firebase import db

app = FastAPI()

# ROUTERS
app.include_router(leads_router, prefix="/api/leads")
app.include_router(automation_router, prefix="/api/automation")
app.include_router(alerts_router, prefix="/api/alerts")
app.include_router(bot_router, prefix="/api/bot")

@app.get("/")
def root():
    return {"status": "backend running"}

# ENDPOINT DE TEST
@app.get("/api/test")
def test():
    return {"status": "ok", "message": "backend vivo"}

# ENDPOINT PARA LANDING (JSON)
@app.post("/api/leads/create")
async def create_lead(request: Request):
    data = await request.json()

    lead = {
        "id": str(uuid.uuid4()),
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "meta": data.get("meta"),
        "created_at": datetime.utcnow().isoformat(),
        "status": "nuevo",
        "source": data.get("source", "landing")
    }

    db.collection("seguro_prospects").document(lead["id"]).set(lead)

    return {"success": True, "lead": lead}

# ENDPOINT PARA STATICFORMS
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

    db.collection("seguro_prospects").document(lead["id"]).set(lead)

    return {"success": True, "lead": lead}
