import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_sql(question, schema):
    """Generates a SQL query from a natural language question."""
    
    prompt = f"""
You are an expert SQL analyst. Given the database schema below, write a SQL query to answer the user's question.

Schema:
{schema}

Question: {question}

Rules:
- Return ONLY the SQL query, nothing else
- No explanations, no markdown, no backticks
- Use only the table and columns defined in the schema
- Keep the query simple and efficient
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text.strip()


def generate_insights(question, sql, results):
    """Generates business insights and Tableau recommendations from query results."""
    
    prompt = f"""
You are a business analyst. A user asked the following question and we ran a SQL query to get results.

Question: {question}

SQL Query used:
{sql}

Results:
{results}

Please provide:
1. A clear plain-English answer to the question (2-3 sentences)
2. 2-3 key business insights from the data
3. A Tableau visualization recommendation (chart type, axes, and why it's the best choice)

Format your response with clear headers for each section.
"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text.strip()