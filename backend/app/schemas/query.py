from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    response: str
    agents_used: List[str]
    task_plan: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
    error: Optional[bool] = False
    error_agent: Optional[str] = None