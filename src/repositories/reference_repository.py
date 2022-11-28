from sqlite3 import IntegrityError
from utils.database_connection import get_database_connection


def parse_ref_type_from_row(row):
    return row["type_name"]

def parse_ref_object_from_row(row):
    ref_object = {
        key: row[key] for key in row.keys()
    }
    return ref_object


class ReferenceRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_ref_type(self, type_name: str):
        cursor = self._connection.cursor()

        try:
            sql = "INSERT INTO reference_types (type_name) VALUES (:t_name)"
            cursor.execute(sql, {"t_name": type_name})
            self._connection.commit()
            new_type_id = cursor.lastrowid
            return new_type_id
        except IntegrityError:
            return None

    def get_ref_type_names(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * from reference_types")

        rows = cursor.fetchall()
        return list(map(parse_ref_type_from_row, rows))

    def get_ref_type_id_by_name(self, type_name: str):
        cursor = self._connection.cursor()

        sql = "SELECT id FROM reference_types id WHERE type_name=:t_name"
        cursor.execute(sql, {"t_name": type_name})
        result = cursor.fetchone()
        if result:
            return result["id"]
        return None

    def check_ref_key_exists(self, ref_key: str):
        cursor = self._connection.cursor()

        sql = "SELECT ref_key FROM latex_references WHERE ref_key=:r_key"
        cursor.execute(sql, {"r_key": ref_key})
        result = cursor.fetchone()
        if result:
            return result[0]
        return None

    def add_reference(self, ref_obj, type_name="BOOK"):
        cursor = self._connection.cursor()

        type_id = self.get_ref_type_id_by_name(type_name)
        if not type_id:
            type_id = self.add_ref_type(type_name)

        sql = "INSERT INTO latex_references \
               (type_id, ref_key, author, editor, title, year, publisher) \
               VALUES (:t_id, :r_key,:auth, :edit, :title, :year, :publ)"

        cursor.execute(sql, {
            "t_id": type_id,
            "r_key": ref_obj["key"],
            "auth": ref_obj["author"],
            "edit": ref_obj["editor"],
            "title": ref_obj["title"],
            "year": ref_obj["year"],
            "publ": ref_obj["publisher"]
        })

        self._connection.commit()

    def get_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * from latex_references")

        rows = cursor.fetchall()
        return list(map(parse_ref_object_from_row, rows))


reference_repository = ReferenceRepository(get_database_connection())
test_reference_repository = ReferenceRepository(
    get_database_connection("test_references.db"))
