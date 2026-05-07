from fastapi import FastAPI
from fastapi.responses import FileResponse

from model import HealthInput,HealthResponse
from predictor import predict_outcome
from chat import generate_health_advice
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],    # ← yeh important hai
    allow_headers=["*"],
)

@app.get("/")
async def serve_ui():
    return FileResponse("health_ui.html")

@app.post("/predict", response_model= HealthResponse)
async def predict_health(input: HealthInput):
    outcome = predict_outcome(
      input.fever,
      input.cough,
      input.fatigue,
      input.difficulty_breathing,
      input.age,
      input.gender,
      input.blood_pressure,
      input.cholesterol
    )

    advice = generate_health_advice(input, outcome)

    return HealthResponse(
    outcome=outcome,
    advice=advice
    )