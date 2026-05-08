from fastapi import FastAPI
from app.routers import enrich, classify

app = FastAPI(
    title="AI-Powered Lead Automation System",
    description="FastAPI backend for lead enrichment and AI intent classification",
    version="1.0.0"
)

app.include_router(enrich.router, tags=["Enrichment"])
app.include_router(classify.router, tags=["AI Classification"])


@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "AI Lead Automation API is active"
    }