import os
from dotenv import load_dotenv
import google.generativeai as genai

# -----------------------------
# Load API Key
# -----------------------------

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# -----------------------------
# Load Gemini Model
# -----------------------------

model = genai.GenerativeModel("gemini-2.5-flash")


# -----------------------------
# Generate SQL Query
# -----------------------------

def generate_sql(user_query):

    prompt = f"""
You are an expert SQL developer.

Convert the following natural language request into SQL.

Return ONLY the SQL query without explanation.

Request:
{user_query}
"""

    response = model.generate_content(prompt)

    return response.text.strip()


# -----------------------------
# Explain SQL Query
# -----------------------------

def explain_sql(sql_query):

    prompt = f"""
You are an expert SQL instructor.

Explain the following SQL query in simple English.

Keep the explanation short (2-4 sentences).

SQL Query:
{sql_query}
"""

    response = model.generate_content(prompt)

    return response.text.strip()