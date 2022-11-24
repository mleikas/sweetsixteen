import sqlite3
import os

database_path = os.path.realpath("../references.db")

connection = sqlite3.connect(database_path)
connection.row_factory = sqlite3.Row
connection.cursor().execute("PRAGMA foreign_keys = ON")


def get_database_connection():
    return connection
