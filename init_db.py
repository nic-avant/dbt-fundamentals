import pathlib
import sqlite3
from sqlite3 import Error

import pandas as pd

HOME = pathlib.Path.home()
PROJECT_PATH = pathlib.Path(HOME, "work", "dbt-fundamentals")


def create_tables(db_file):
    conn = sqlite3.connect(db_file)

    customers = pd.read_csv(
        str(pathlib.Path(PROJECT_PATH, "data", "jaffle_shop_customers.csv"))
    )
    customers.to_sql("customers", conn, schema="jaffle_shop", if_exists="replace")

    orders = pd.read_csv(
        str(pathlib.Path(PROJECT_PATH, "data", "jaffle_shop_orders.csv"))
    )
    orders.to_sql("orders", conn, schema="jaffle_shop", if_exists="replace")

    payments = pd.read_csv(
        str(pathlib.Path(PROJECT_PATH, "data", "stripe_payments.csv"))
    )
    payments.to_sql("payments", conn, schema="jaffle_shop", if_exists="replace")


def create_connection(db_file):
    """create a database connection to a SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    create_connection(f"{PROJECT_PATH}/data/db.db")
    create_tables(f"{PROJECT_PATH}/data/db.db")
