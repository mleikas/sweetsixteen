import sqlite3
from pathlib import Path


def build_connection(db_name):

    file_path = Path(__file__).parent.parent
    database_path = file_path / db_name

    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.cursor().execute("PRAGMA foreign_keys = ON")

    return connection


def get_database_connection(db_name="references.db"):
    return build_connection(db_name)
