from pathlib import Path

if __name__ == "__main__":
    from database_connection import get_database_connection
else:
    from .database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    tables = ["reference_types", "latex_references",
              "reference_entries", "field_types"]

    for table in tables:
        sql = "DROP TABLE IF EXISTS " + table + ";"
        cursor.execute(sql)
        connection.commit()


def create_tables(connection):
    schema_path = Path(__file__).parent / "schema.sql"
    schema_script = open(schema_path, "r").read()
    cursor = connection.cursor()
    cursor.executescript(schema_script)
    connection.commit()


def initialize_database(db_name="references.db"):
    connection = get_database_connection(db_name)
    drop_tables(connection)
    create_tables(connection)
    return connection


if __name__ == "__main__":
    initialize_database()
