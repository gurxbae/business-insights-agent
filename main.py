import os
import sys
from agent.db_manager import load_csv_to_db, get_schema, run_query
from agent.sql_generator import generate_sql, generate_insights
from agent.insights import format_results

def main():
    print("=" * 55)
    print("   Business Insights Agent")
    print("=" * 55)

    # Step 1 - Load CSV into database
    print("\n[1/4] Loading sales data into database...")
    try:
        columns = load_csv_to_db()
        print(f"      Columns: {', '.join(columns)}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Step 2 - Get schema
    print("\n[2/4] Reading database schema...")
    schema = get_schema()
    print(schema)

    # Step 3 - Ask user for a business question
    print("=" * 55)
    print("Ask a business question about the sales data.")
    print("Examples:")
    print("  - Which product category has the highest revenue?")
    print("  - What are the top 5 states by total sales?")
    print("  - Which shipping mode is used most frequently?")
    print("=" * 55)
    question = input("\nYour question: ").strip()

    if not question:
        print("No question entered. Exiting.")
        sys.exit(1)

    # Step 4 - Generate and run SQL
    print("\n[3/4] Generating SQL query...")
    sql = generate_sql(question, schema)
    print(f"\n Generated SQL:\n{sql}")

    print("\n Running query...")
    try:
        results_df = run_query(sql)
        formatted = format_results(results_df)
        print(f"\n Query Results:\n{formatted}")
    except Exception as e:
        print(f"Error running query: {e}")
        sys.exit(1)

    # Step 5 - Generate insights
    print("\n[4/4] Generating business insights...")
    insights = generate_insights(question, sql, formatted)

    print("\n" + "=" * 55)
    print("   BUSINESS INSIGHTS")
    print("=" * 55)
    print(insights)

if __name__ == "__main__":
    main()