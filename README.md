# AI Health Assistant 🏥

AI-powered health analysis system using Machine Learning + LLM.

## Live Demo
🌐 https://ai-health-assistant-mvoq.onrender.com

## What it does
- Predicts health outcome: Positive/Negative using ML
- Generates AI health advice using Groq + Llama 3.3
- 80% accuracy on symptom dataset
- Professional disclaimer included

## Tech Stack
- Python, FastAPI
- Scikit-learn (Random Forest — 80% accuracy)
- Groq API (Llama 3.3 70B)
- Pandas, NumPy, Joblib
- Pydantic

## API Endpoint
- `GET  /`        → UI
- `POST /predict` → ML Prediction + AI Advice
- `GET  /docs`    → API Documentation

## Run Locally
git clone https://github.com/RahilMirchiwala/AI-Health-Assistant
cd AI-Health-Assistant
pip install -r requirements.txt
uvicorn main:app --reload

## Environment Variables
GROQ_API_KEY=your_key_here

## Disclaimer
This is AI-generated advice only.
Please consult a qualified medical professional.