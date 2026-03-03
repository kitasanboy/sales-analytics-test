from pathlib import Path
from sqlite3 import Connection
import pandas as pd

def compute_revenue_per_customer_month(conn: Connection) -> pd.DataFrame:
    # TODO: Write your SQL query here to generate the revenue per customer per month report here.
    #
    # query = """
    # SELECT ...
    # """
    # return pd.read_sql_query(query, conn)

    # TODO: Remove this placeholder code and replace it with the implementation above.
    df = pd.DataFrame(columns=["customer_id", "name", "country", "year_month", "revenue"])
    df.loc[0] = [6, "Quantum Analytics", "US", "2025-01", 3200]  # Sample row
    return df

def compute_top_products(conn: Connection, limit: int = 5) -> pd.DataFrame:
    # TODO: Write your SQL query here to generate the top products report here.
    #
    # query = """
    # SELECT ...
    # """
    # return pd.read_sql_query(query, conn, params=(limit,))

    # TODO: Remove this placeholder code and replace it with the implementation above.
    df = pd.DataFrame(columns=["product_name", "total_revenue"])
    df.loc[0] = ["Laptop Pro", 6000]  # Sample row
    return df

def generate_reports(conn: Connection, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    df_rev = compute_revenue_per_customer_month(conn)
    df_rev.to_csv(output_dir / "revenue_per_customer_per_month.csv", index=False)

    df_top = compute_top_products(conn, limit=5)
    df_top.to_csv(output_dir / "top_products.csv", index=False)
