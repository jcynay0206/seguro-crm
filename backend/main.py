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
