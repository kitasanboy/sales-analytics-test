from pathlib import Path
from sqlite3 import Connection
import pandas as pd

from .config import DATA_DIR

def load_all_data(conn: Connection) -> None:
    load_customers(conn)
    load_orders(conn)
    load_order_items(conn)

def load_customers(conn: Connection) -> None:
    df = pd.read_csv(Path(DATA_DIR) / "customers.csv")
    df.to_sql("customers", conn, if_exists="replace", index=False)

def load_orders(conn: Connection) -> None:
    df = pd.read_csv(Path(DATA_DIR) / "orders.csv")
    df.to_sql("orders", conn, if_exists="replace", index=False)

def load_order_items(conn: Connection) -> None:
    df = pd.read_csv(Path(DATA_DIR) / "order_items.csv")
    df.to_sql("order_items", conn, if_exists="replace", index=False)
