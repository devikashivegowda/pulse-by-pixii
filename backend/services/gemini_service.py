import os
from google import genai
import json

def query_gemini(query):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
    Give top 5 real products for: {query}

    Return STRICT JSON like:
    [
      {{
        "name": "Product Name",
        "reason": "Why recommended"
      }}
    ]
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    try:
        return json.loads(response.text)
    except:
        return []