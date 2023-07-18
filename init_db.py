import pathlib
import sqlite3
from sqlite3 import Error

import pandas as pd

HOME = pathlib.Path.home()
PROJECT_PATH = pathlib.Path(HOME, "work", "dbt-fundamentals")


def create_tables(jaffle_shop_db, stripe_db):
    conn = sqlite3.connect(jaffle_shop_db)

    customers = pd.read_csv(
        str(pathlib.Path(PROJECT_PATH, "data", "jaffle_shop_customers.csv"))
    )
    customers.to_sql("customers", conn, schema="main", if_exists="replace")

    orders = pd.read_csv(
        str(pathlib.Path(PROJECT_PATH, "data", "jaffle_shop_orders.csv"))
    )
    orders.to_sql("orders", conn, schema="main", if_exists="replace")

    conn = sqlite3.connect(stripe_db)

    payments = pd.read_csv(
        str(pathlib.Path(PROJECT_PATH, "data", "stripe_payments.csv"))
    )
    payments.to_sql("payments", conn, schema="main", if_exists="replace")


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
    jaffle_shop_db = f"{PROJECT_PATH}/data/jaffle_shop.db"
    stripe_db = f"{PROJECT_PATH}/data/stripe.db"
    # sqlite has 1 schema, so using multiple sqlite databases kind of mimics
    # multiple schemas in larger data store
    create_connection(jaffle_shop_db)
    create_connection(stripe_db)
    create_tables(jaffle_shop_db, stripe_db)
