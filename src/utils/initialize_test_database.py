from utils.initialize_database import initialize_database


def create_tables(connection):
    cursor = connection.cursor()
    cursor.executescript("""
        INSERT INTO reference_types (type_name) VALUES ("book");

        INSERT INTO latex_references 
            (ref_key, type_id, author, title, year, publisher) VALUES
            ("BOOK123", 1, "Author1", "Title1", 2022, "Publisher1"); 

        INSERT INTO latex_references 
            (ref_key, type_id, editor, title, year, publisher) VALUES
            ("BOOK124", 1, "Editor2", "Title2", 2022, "Publisher2"); 

    """)
    connection.commit()


def initialize_test_database():
    connection = initialize_database("test_references.db")
    create_tables(connection)
    connection.close()


if __name__ == "__main__":
    initialize_test_database()
