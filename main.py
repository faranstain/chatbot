
from fastapi import FastAPI, HTTPException
from models import Query, Response
from api import GeminiAPI
import string

app = FastAPI()
gemini_api = GeminiAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Gemini API"}

@app.post("/generate", response_model=Response)
async def generate_response(query: Query):
    try:
        response = gemini_api.get_response(query.user_query)
        return Response(llm_response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app", host="127.0.0.1", port=8008,workers=2, reload=True  
    )
