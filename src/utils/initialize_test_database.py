from utils.initialize_database import initialize_database


def initialize_test_database():
    connection = initialize_database("test_references.db")
    connection.close()


if __name__ == "__main__":
    initialize_test_database()
