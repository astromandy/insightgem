import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(prompt: str, preview: str, context: list = None) -> str:
    model = genai.GenerativeModel("gemini-pro")
    history = "\n".join([f"Q: {c['question']}\nA: {c['code']}" for c in context]) if context else ""
    
    full_prompt = f"""
You are a Python data analyst. Given the user's question and a pandas DataFrame (df),
write Python code to answer the question using pandas.

Only return valid Python code — no explanation or markdown.

{history}

DataFrame Preview:
{preview}

User question:
{prompt}
"""

    response = model.generate_content(full_prompt)
    return response.text.strip("```python").strip("```").strip()

