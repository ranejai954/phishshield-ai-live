from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=api_key
)


def analyze_phishing(text):

    if not api_key:
        return {
            "threat_level": "ERROR",
            "risk_score": 0,
            "indicators": [],
            "explanation": "GROQ_API_KEY not configured.",
            "recommendations": [
                "Configure your API key."
            ]
        }

    prompt = f"""
You are a cybersecurity expert specializing in phishing detection.

Analyze the following message:

{text}

Return ONLY valid JSON in the exact format below.

{{
    "threat_level": "LOW|MEDIUM|HIGH|CRITICAL",
    "risk_score": 0,
    "indicators": [],
    "explanation": "",
    "recommendations": []
}}

Rules:
- Return ONLY JSON
- No markdown
- No code blocks
- No extra text
- Risk score must be between 0 and 100
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        result = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

        return json.loads(result)

    except json.JSONDecodeError:

        return {
            "threat_level": "ERROR",
            "risk_score": 0,
            "indicators": [],
            "explanation": "Failed to parse AI response.",
            "recommendations": [
                "Try analyzing again."
            ]
        }

    except Exception as e:

        return {
            "threat_level": "ERROR",
            "risk_score": 0,
            "indicators": [],
            "explanation": str(e),
            "recommendations": [
                "Check API configuration."
            ]
        }