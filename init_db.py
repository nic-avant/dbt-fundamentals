import pathlib
import sqlite3
from sqlite3 import Error

HOME = pathlib.Path.home()
PROJECT_PATH = pathlib.Path(HOME, "work", "dbt-fundamentals")


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
