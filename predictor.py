import joblib
import pandas as pd

# Load Model
model = joblib.load('health_model.pkl')
encoders = joblib.load('encoders.pkl')
target_encoder = joblib.load('target_encoder.pkl')

def predict_outcome(fever: str, cough: str, fatigue: str,difficulty_breathing: str, age: int,
                    gender: str, blood_pressure: str, cholesterol: str) -> str:
  input_data = {
    'Fever': fever,
    'Cough': cough,
    'Fatigue': fatigue,
    'Difficulty Breathing': difficulty_breathing,
    'Age': age,
    'Gender': gender,
    'Blood Pressure': blood_pressure,
    'Cholesterol Level': cholesterol
  }

  for col in encoders:
    input_data[col] = encoders[col].transform([input_data[col]])[0]

  df = pd.DataFrame([input_data])

  prediction = model.predict(df)[0]

  result = target_encoder.inverse_transform([prediction])[0]

  return result

result = predict_outcome(
    fever="Yes", cough="Yes", fatigue="Yes",
    difficulty_breathing="Yes", age=25,
    gender="Female", blood_pressure="High",
    cholesterol="Normal"
)
print(result)