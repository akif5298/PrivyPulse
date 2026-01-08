from fastapi import APIRouter
from app.schemas.query import QueryRequest, QueryResponse
from app.agents.coordinator import run_workflow

router = APIRouter(prefix = "/query", tags = ["Query"])

@router.post("/", response_model = QueryResponse)
def query_system(request: QueryRequest):
    output = run_workflow(request.query)
    return output