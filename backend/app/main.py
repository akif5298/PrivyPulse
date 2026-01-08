from fastapi import FastAPI
from app.api.query import router as query_router

app = FastAPI(title = "PrivyPulse", description = "Privacy-Preserving Market Research Assistant")

app.include_router(query_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
