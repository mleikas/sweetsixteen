from functools import reduce
from utils.database_connection import get_database_connection


def parse_ref_type_from_row(row):
    return row["type_name"]


def parse_ref_object_from_row(row):
    ref_object = {
        key: row[key] for key in row.keys()
    }
    return ref_object


def parse_entry(row):
    return {
        row["type_name"]: row["value"]
    }


class ReferenceRepository:
    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor()

    def get_ref_type_names(self):
        self._cursor.execute("SELECT * from reference_types")

        rows = self._cursor.fetchall()
        return list(map(parse_ref_type_from_row, rows))

    def get_id_of_reference_type_by_name(self, type_name: str):
        sql = "SELECT id FROM reference_types id WHERE type_name=:t_name"
        self._cursor.execute(sql, {"t_name": type_name})
        result = self._cursor.fetchone()
        if result:
            return result["id"]
        return None

    def get_name_of_reference_type_by_id(self, type_id: int):
        sql = "SELECT type_name FROM reference_types WHERE id=:t_id"
        self._cursor.execute(sql, {"t_id": type_id})
        result = self._cursor.fetchone()
        if result:
            return result["type_name"]
        return None

    def get_id_of_field_type_by_name(self, field_name: str):
        sql = "SELECT id FROM field_types id WHERE type_name=:t_name"
        self._cursor.execute(sql, {"t_name": field_name})
        result = self._cursor.fetchone()
        if result:
            return result["id"]
        return None

    def get_field_types_by_name(self, type_name:str):
        ref_type_id=self.get_id_of_reference_type_by_name(type_name)
        sql = "SELECT type_name, required FROM field_types \
               WHERE ref_type_id=:ref_type_id ORDER BY required DESC"
        self._cursor.execute(sql, {"ref_type_id": ref_type_id})
        rows = self._cursor.fetchall()
        references=list(map(parse_ref_object_from_row, rows))
        new_references = {}
        for ref in references:
            new_references[ref['type_name']] = ref["required"]
        return new_references


    def check_ref_key_exists(self, ref_key: str):
        sql = "SELECT ref_key FROM latex_references WHERE ref_key=:r_key"
        self._cursor.execute(sql, {"r_key": ref_key})
        result = self._cursor.fetchone()
        if result:
            return result[0]
        return None

    def add_reference_entries(self, ref_obj, ref_id):
        sql = "INSERT INTO reference_entries (type_id, ref_id, value) \
               VALUES (:type_id, :ref_id, :value);"

        for key in ref_obj:
            if key not in ["type_id", "ref_key"]:
                field_type_id = self.get_id_of_field_type_by_name(key)
                self._cursor.execute(sql, {
                    "type_id": field_type_id,
                    "ref_id": ref_id,
                    "value": ref_obj[key]
                })

        self._connection.commit()

    def add_reference(self, ref_obj, type_name):
        type_id = self.get_id_of_reference_type_by_name(type_name)

        sql = "INSERT INTO latex_references \
               (type_id, ref_key) \
               VALUES (:t_id, :r_key)"

        self._cursor.execute(sql, {
            "t_id": type_id,
            "r_key": ref_obj["key"]
        })
        self._connection.commit()
        return self._cursor.lastrowid

    def delete_reference(self, r_key: str):
        sql = "DELETE FROM latex_references WHERE ref_key=:r_key"
        self._cursor.execute(sql, {"r_key": r_key})

        self._connection.commit()

    def get_all_references(self):
        self._cursor.execute("SELECT * from latex_references")

        rows = self._cursor.fetchall()
        return list(map(parse_ref_object_from_row, rows))

    def get_reference_with_key(self, ref_key):
        sql = "SELECT * from latex_references WHERE ref_key == (:ref_key)"
        self._cursor.execute(sql, {"ref_key": ref_key})
        row = self._cursor.fetchone()

        return parse_ref_object_from_row(row)

    def get_reference_entries(self, ref_id):
        sql = "SELECT B.type_name, A.value from reference_entries A, field_types B \
            WHERE A.ref_id == (:ref_id) AND A.value IS NOT NULL AND A.type_id == B.id; "

        self._cursor.execute(sql, {
            "ref_id": ref_id
        })

        rows = self._cursor.fetchall()
        if rows:
            list_of_entries = map(parse_entry, rows)
            return reduce(lambda a, b: {**a, **b}, list_of_entries)
        return {}

    def get_all_references_with_entries(self):
        reference_list = self.get_all_references()
        return list(map(
            lambda ref_object: {
                **ref_object,
                **self.get_reference_entries(ref_object["id"])
            },
            reference_list))


reference_repository = ReferenceRepository(get_database_connection())
test_reference_repository = ReferenceRepository(
    get_database_connection("test_references.db"))
