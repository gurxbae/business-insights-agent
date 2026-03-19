from tabulate import tabulate

def format_results(df):
    """Formats a dataframe into a readable table string."""
    if df.empty:
        return "No results found."
    
    # Limit to 20 rows for display
    display_df = df.head(20)
    return tabulate(display_df, headers="keys", tablefmt="grid", showindex=False)