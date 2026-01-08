from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.query import router as query_router

app = FastAPI(title = "PrivyPulse", description = "Privacy-Preserving Market Research Assistant")

# Configure CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
