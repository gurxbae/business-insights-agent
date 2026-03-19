import sqlite3
import pandas as pd
import os

DB_PATH = "sales.db"

def load_csv_to_db():
    """Loads the sales CSV into a SQLite database."""
    
    # Find the CSV file
    csv_file = None
    for f in os.listdir("."):
        if f.endswith(".csv"):
            csv_file = f
            break
    
    if not csv_file:
        raise FileNotFoundError("No CSV file found in the project folder.")
    
    print(f"      Loading {csv_file} into database...")
    df = pd.read_csv(csv_file, encoding="latin-1")
    
    # Clean column names - remove spaces and special characters
    df.columns = df.columns.str.replace(" ", "_").str.replace("-", "_").str.lower()
    
    conn = sqlite3.connect(DB_PATH)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()
    
    print(f"      Loaded {len(df)} rows into 'sales' table.")
    return df.columns.tolist()

def get_schema():
    """Returns the schema of the sales table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(sales)")
    columns = cursor.fetchall()
    conn.close()
    
    schema = "Table: sales\nColumns:\n"
    for col in columns:
        schema += f"  - {col[1]} ({col[2]})\n"
    return schema

def run_query(sql):
    """Runs a SQL query and returns results as a list of dicts."""
    conn = sqlite3.connect(DB_PATH)
    try:
        df = pd.read_sql_query(sql, conn)
        conn.close()
        return df
    except Exception as e:
        conn.close()
        raise e