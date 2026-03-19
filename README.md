# Business Insights Agent

An agentic AI that answers plain-English business questions using SQL and 
generates actionable insights with Tableau visualization recommendations — 
turning raw sales data into business intelligence instantly.

## What it does
- Loads real sales data (9,800 rows) into a SQLite database automatically
- Accepts plain-English business questions from the user
- Generates and runs the correct SQL query automatically
- Returns a formatted results table
- Produces business insights and exact Tableau chart recommendations using Claude AI

## Tech Stack
Python, Anthropic Claude API, SQLite, pandas, tabulate, python-dotenv

## How to run
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Anthropic API key to `.env` as `ANTHROPIC_API_KEY=your_key`
4. Add your sales CSV file to the project folder
5. Run: `python main.py`
6. Type any business question when prompted

## Example Questions
- "Which product category has the highest revenue?"
- "What are the top 5 states by total sales?"
- "Which shipping mode is used most frequently?"
- "What is the monthly revenue trend?"

## Sample Output
**Question:** Which product category has the highest revenue?
**Generated SQL:** `SELECT category, SUM(sales) AS total_revenue FROM sales GROUP BY category ORDER BY total_revenue DESC LIMIT 1`
**Answer:** Technology leads with $827,456 in total revenue, making it the core revenue driver of the business.

## Dataset
Retail sales dataset (9,800 rows) with order details, customer segments, 
product categories, regional data and sales figures.