
from pydantic import BaseModel

class Query(BaseModel):
    user_query: str

class Response(BaseModel):
    llm_response: str