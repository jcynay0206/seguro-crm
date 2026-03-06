from fastapi import FastAPI
from backend.routes.leads import router as leads_router
from backend.routes.automation import router as automation_router
from backend.routes.alerts import router as alerts_router
from backend.routes.bot import router as bot_router

app = FastAPI()


app.include_router(leads_router, prefix="/api/leads")
app.include_router(automation_router, prefix="/api/automation")
app.include_router(alerts_router, prefix="/api/alerts")
app.include_router(bot_router, prefix="/api/bot")

@app.get("/")
def root():
    return {"status": "backend running"}
from routes import calendly
app.include_router(calendly.router)
from fastapi import Request
from datetime import datetime
import uuid

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

    # Guardar en Firebase
    db.collection("leads").document(lead["id"]).set(lead)

    return {"success": True, "lead": lead}

