import sqlite3
from pathlib import Path

file_path = Path(__file__).parent.parent
database_path = file_path / "references.db"

connection = sqlite3.connect(database_path)
connection.row_factory = sqlite3.Row
connection.cursor().execute("PRAGMA foreign_keys = ON")


def get_database_connection():
    return connection
