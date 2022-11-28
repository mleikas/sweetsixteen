from utils.database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    tables = ["latex_references", "fields", "reference_types"]

    for table in tables:
        sql = "DROP TABLE IF EXISTS " + table + ";"
        cursor.execute(sql)
        connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.executescript("""
        CREATE TABLE reference_types (
            id INTEGER PRIMARY KEY,
            type_name TEXT UNIQUE
        );

        CREATE TABLE latex_references (
            id INTEGER PRIMARY KEY,
            ref_key TEXT UNIQUE,
            type_id INTEGER 
                REFERENCES reference_types
                ON DELETE CASCADE,
            author TEXT,
            editor TEXT,
            title TEXT,
            year INTEGER,
            publisher TEXT
        );

    """)
    connection.commit()


def initialize_database(db_name="references.db"):
    connection = get_database_connection(db_name)
    drop_tables(connection)
    create_tables(connection)
    return connection


if __name__ == "__main__":
    initialize_database()
