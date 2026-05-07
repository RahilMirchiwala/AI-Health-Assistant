from pydantic import BaseModel
from typing import Literal

class HealthInput(BaseModel):
    fever: Literal["Yes", "No"]
    cough: Literal["Yes", "No"]
    fatigue: Literal["Yes", "No"]
    difficulty_breathing: Literal["Yes", "No"]

    age: int

    gender: Literal["Male", "Female"]

    blood_pressure: Literal["Low", "Normal", "High"]

    cholesterol: Literal["Low", "Normal", "High"]

class HealthResponse(BaseModel):
    outcome: Literal["Positive", "Negative"]
    advice: str