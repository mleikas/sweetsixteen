from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    tables = ["reference_types", "fields", "latex_references"]

    for table in tables:
        sql = "DROP TABLE IF EXISTS " + table + ";"
        cursor.execute(sql)
        connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.executescript("""
        CREATE TABLE reference_types (
            id INTEGER PRIMARY KEY,
            type_name TEXT 
        );

        CREATE TABLE latex_references (
            id INTEGER PRIMARY KEY,
            ref_key TEXT UNIQUE,
            type_id INTEGER REFERENCES reference_types,
            author TEXT,
            editor TEXT,
            title TEXT,
            year INTEGER,
            publisher TEXT
        );

    """)
    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
