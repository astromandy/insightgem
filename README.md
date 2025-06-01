# InsightGem

An advanced AI-powered data exploration app using **Gemini** and the **Davia SDK**.

## 🔍 Features

- Upload a CSV file
- Preview the data and generate statistics
- Ask natural language questions about your dataset
- Gemini generates pandas code to answer your question
- Code is executed securely and results shown
- Includes data profiling (missing values, correlations)
- Remembers your previous questions in context

## 💡 Example Prompts

- "What are the top 5 products by price?"
- "How many null values are in each column?"
- "Calculate average salary per department."

## ⚙️ Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Create a `.env` file and add your Gemini API key:

```
GEMINI_API_KEY=your-key-here
```

## 🌐 Deploy on Render

Includes a `render.yaml` file for 1-click deployment.

---

Built for the Davia AI job application challenge.
