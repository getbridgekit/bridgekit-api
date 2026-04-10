from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bridgekit import evaluate, plan, ask

# Create the app
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the Bridgekit API, fellow data nerds! -Iva"}


# Define request shape for evaluate()
class EvaluateRequest(BaseModel):
    text: str


# Create an endpoint
@app.post("/evaluate")
def evaluate_writeup(request: EvaluateRequest):
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
def plan_analysis(request: PlanRequest):
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
def ask_question(request: AskRequest):
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
