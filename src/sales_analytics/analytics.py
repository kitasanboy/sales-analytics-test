from pathlib import Path
from sqlite3 import Connection
import pandas as pd


def compute_revenue_per_customer_month(conn: Connection) -> pd.DataFrame:
    query = """
        SELECT
            c.customer_id,
            c.name,
            c.country,
            strftime('%Y-%m', o.order_date) AS year_month,
            ROUND(SUM(o.total_amount), 2)   AS revenue
        FROM orders o
        JOIN customers c ON c.customer_id = o.customer_id
        WHERE o.total_amount >= 0
        GROUP BY c.customer_id, c.name, c.country, year_month
        ORDER BY year_month ASC, revenue DESC
    """
    return pd.read_sql_query(query, conn)


def compute_top_products(conn: Connection, limit: int = 5) -> pd.DataFrame:
    query = """
        SELECT
            oi.product_name,
            ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue
        FROM order_items oi
        GROUP BY oi.product_name
        ORDER BY total_revenue DESC
        LIMIT ?
    """
    return pd.read_sql_query(query, conn, params=(limit,))


def generate_reports(conn: Connection, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    df_rev = compute_revenue_per_customer_month(conn)
    df_rev.to_csv(output_dir / "revenue_per_customer_per_month.csv", index=False)
    df_top = compute_top_products(conn, limit=5)
    df_top.to_csv(output_dir / "top_products.csv", index=False)