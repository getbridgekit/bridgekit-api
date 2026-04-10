import os
from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from bridgekit import evaluate, plan, ask

# Create the app
app = FastAPI()

# API key auth
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def require_api_key(key: str = Security(api_key_header)):
    expected = os.environ.get("BRIDGEKIT_API_KEY")
    if not expected or key != expected:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return key


@app.get("/")
def root():
    return {"message": "Welcome to the Bridgekit API, fellow data nerds! -Iva"}


# Define request shape for evaluate()
class EvaluateRequest(BaseModel):
    text: str


# Create an endpoint
@app.post("/evaluate")
def evaluate_writeup(request: EvaluateRequest, key: str = Depends(require_api_key)):
    try:
        result = evaluate(request.text)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except EnvironmentError as e:
        raise HTTPException(status_code=500, detail=str(e))

#Define shape for plan()
class PlanRequest(BaseModel):
    question: str
    data_description: str = None
    goal: str = None

#Create endpoint for plan()
@app.post("/plan")
def plan_analysis(request: PlanRequest, key: str = Depends(require_api_key)):
    try:
        result = plan(
            question=request.question,
            data_description=request.data_description,
            goal=request.goal
        )
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except EnvironmentError as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define shape for ask()
class AskRequest(BaseModel):
    question: str
    text: str = None
    source: str = None

# Create endpoint for ask()
@app.post("/ask")
def ask_question(request: AskRequest, key: str = Depends(require_api_key)):
    try:
        result = ask(
            question=request.question,
            text=request.text,
            source=request.source
        )
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except EnvironmentError as e:
        raise HTTPException(status_code=500, detail=str(e))
