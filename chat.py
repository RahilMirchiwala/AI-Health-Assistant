import os
import sys
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
sys.stdout.reconfigure(encoding='utf-8')  

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_health_advice(symptoms, outcome: str) -> str:

    system_prompt  = """
    You are a Health Assistant AI.
    Analyze the patient's symptoms and provide:
    1. Possible conditions
    2. What to do next
    3. When to see a doctor
    """

    user_prompt = f"""
    Fever: {symptoms.fever}
    Cough: {symptoms.cough}
    Fatigue: {symptoms.fatigue}
    Difficulty Breathing: {symptoms.difficulty_breathing}
    Age: {symptoms.age}
    Gender: {symptoms.gender}
    Blood Pressure: {symptoms.blood_pressure}
    Cholesterol: {symptoms.cholesterol}

    Predicted Outcome: {outcome}

    ⚠️ Always add: This is not medical advice. Consult a doctor.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content