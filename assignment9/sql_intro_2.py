import pandas as pd 
import sqlite3 

# Task 5: Read Data into a DataFrame
try:
    with sqlite3.connect("db/lesson.db") as conn:
        # Read into a DataFrame
        sql_statement = """SELECT l.line_item_id, l.quantity, l.product_id, p.product_name, p.price FROM line_items l JOIN products p ON l.product_id = p.product_id"""
        df = pd.read_sql_query(sql_statement, conn)

        # Print first 5 lines
        print("----------Original DataFrame----------")
        print(df.head())

        # Add a column to DataFrame called "total"
        df["total"] = df["quantity"] * df["price"]

        # Print first 5 lines to see new colummn
        print("----------Updated DataFrame with new column 'Total'----------")
        print(df.head())

        # Add groupby() to group by the product_id 
        # Print first 5 lines of new DataFrame
        print("----------Updated DataFrame with groupby()----------")
        print(df.groupby("product_id").agg({"line_item_id": "count", "total": "sum", "product_name": "first"}).head())

        # Sort DataFrame by product_name 
        df_sorted = df.sort_values("product_name")

        # Write to CSV file
        df_sorted.to_csv("assignment9/order_summary.csv")
except Exception as e:
    print(f"Exception caught: {e}")

