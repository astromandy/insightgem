import os
import pandas as pd
from dotenv import load_dotenv
from davia import Davia

from llm_agent import ask_gemini
from pandas_executor import safe_pandas_eval
from profiling import generate_profile

load_dotenv()

session_context = {}

def insightgem(file=None, question=None, follow_up=None):
    if file is None:
        return {
            "📊 Data Preview": "Please upload a CSV file.",
            "🧠 Suggested Code": "",
            "✅ Execution Result": "",
            "📌 Data Profile": ""
        }

    df = pd.read_csv(file)
    df_preview = df.head().to_markdown()

    profile = generate_profile(df)

    context = session_context.get("history", [])
    prompt = question or follow_up or "Give me insights from this dataset."

    try:
        code = ask_gemini(prompt, df_preview, context)
        result = safe_pandas_eval(code, df)
        session_context["history"] = context + [{"question": prompt, "code": code}]
    except Exception as e:
        result = f"Error: {str(e)}"
        code = "Code generation failed."

    return {
        "📊 Data Preview": df_preview,
        "🧠 Suggested Code": f"```python\n{code}```",
        "✅ Execution Result": result,
        "📌 Data Profile": profile
    }

Davia(
    inputs=[
        {"name": "file", "type": "file"},
        {"name": "question", "type": "text"},
        {"name": "follow_up", "type": "text"}
    ],
    outputs=[
        {"name": "📊 Data Preview", "type": "markdown"},
        {"name": "🧠 Suggested Code", "type": "code"},
        {"name": "✅ Execution Result", "type": "text"},
        {"name": "📌 Data Profile", "type": "markdown"}
    ],
    flow=insightgem
    port=port
)
