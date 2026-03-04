from fastapi import FastAPI
from routes.leads import router as leads_router
from routes.automation import router as automation_router
from routes.alerts import router as alerts_router
from routes.bot import router as bot_router

app = FastAPI()

app.include_router(leads_router, prefix="/api/leads")
app.include_router(automation_router, prefix="/api/automation")
app.include_router(alerts_router, prefix="/api/alerts")
app.include_router(bot_router, prefix="/api/bot")

@app.get("/")
def root():
    return {"status": "backend running"}
