import unittest
from utils.initialize_test_database import initialize_test_database
from repositories.reference_repository import test_reference_repository as ref_repository

BOOK_ENTRY_DATA = {
    "address": "Osoite123",
    "author": "Authori",
    "edition": "1",
    "editor": "Editor123",
    "month": "January",
    "note": "This is a note",
    "number": "4",
    "publisher": "Otava",
    "series": "Series?",
    "title": "Muumit laaksossa",
    "volume": "2",
    "year": "2022"
}


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        # initilizes the database and inserts two references into the database
        initialize_test_database()
        self._ref_repository = ref_repository
        self._ref_repository.add_reference(
            {"key": "BOOK123", "type_id": 1}, "book")
        self._ref_repository.add_reference(
            {"key": "BOOK124", "type_id": 1}, "book")
        self._ref_repository.add_reference_entries(BOOK_ENTRY_DATA, 1)

    def test_get_all_reference_type_from_database(self):
        types_in_database = self._ref_repository.get_ref_type_names()
        ref_types = ['book', 'article', 'misc', 'phdthesis', 'incollection']
        self.assertListEqual(types_in_database, ref_types)

    def test_get_all_references_from_database(self):
        references = self._ref_repository.get_all_references()

        self.assertEqual(references[0]["ref_key"], "BOOK123")
        self.assertEqual(references[1]["ref_key"], "BOOK124")

    def test_get_reference_with_key_from_database(self):
        reference = self._ref_repository.get_reference_with_key("BOOK123")

        self.assertEqual(reference["ref_key"], "BOOK123")

    def test_adding_book_reference_with_valid_data_adds_book_to_database(self):
        new_book = {
            "key": "auth2022ABBT",
            "type_id": 1
        }

        self._ref_repository.add_reference(new_book, "book")

        ref_list = self._ref_repository.get_all_references()
        self.assertEqual(len(ref_list), 3)

    def test_adding_book_entries(self):
        ref_data = {"type_id": 1, "ref_key": "BOOK124"}
        book_entries = {
            "address": "Osoite123",
            "author": "Authori",
            "edition": "1",
            "editor": "Editor123",
            "month": "January",
            "note": "This is a note",
            "number": "4",
            "publisher": "Otava",
            "series": "Series?",
            "title": "Muumit laaksossa",
            "volume": "2",
            "year": "2022"
        }

        self._ref_repository.add_reference_entries(
            {**ref_data, **book_entries}, 2)
        result = self._ref_repository.get_reference_entries(2)

        self.assertEqual(result["address"], "Osoite123")
        self.assertDictEqual(book_entries, result)

    def test_get_all_references_with_entries(self):
        ref_data = {"id": 1, "type_id": 1,
                    "ref_key": "BOOK123", **BOOK_ENTRY_DATA}
        ref_list = self._ref_repository.get_all_references_with_entries()

        self.assertEqual(len(ref_list), 2)
        self.assertDictEqual(ref_data, ref_list[0])

    def test_deleting_reference_removes_reference_info_from_latex_references_table(self):
        ref_info = {
            "key": "auth1973",
            "type_id": 1,
        }

        self._ref_repository.add_reference(ref_info, "book")

        self._ref_repository.delete_reference("auth1973")
        result = self._ref_repository.get_all_references()

        self.assertEqual(len(result), 2)
        for stored_ref in result:
            self.assertNotEqual(stored_ref["ref_key"], "auth1973")

    def test_deleting_reference_removes_all_related_data_from_reference_entries_table(self):
        ref_info = {
            "key": "auth1973",
            "type_id": 1,
        }

        ref_id = self._ref_repository.add_reference(ref_info, "book")

        ref_data = {"type_id": 1, "ref_key": "auth1973"}
        book_entries = {
            "address": "Book Lane 1",
            "author": "Annie Author",
            "edition": "1",
            "editor": "Eddie Editor",
            "month": "January",
            "note": "This is a note",
            "number": "4",
            "publisher": "Publisher Publishing Ltd",
            "series": "Series?",
            "title": "The Best Book Ever",
            "volume": "2",
            "year": "1979"
        }

        self._ref_repository.add_reference_entries(
            {**ref_data, **book_entries},
            ref_id
        )

        self._ref_repository.delete_reference("auth1973")
        result = self._ref_repository.get_reference_entries(ref_id)

        self.assertEqual(result, {})

    def test_check_for_existing_cite_key_returns_cite_key_if_key_exists(self):
        returned_key = self._ref_repository.check_ref_key_exists("BOOK123")
        self.assertEqual(returned_key, "BOOK123")

    def test_check_for_existing_cite_key_returns_None_if_key_does_not_exist(self):
        returned_key = self._ref_repository.check_ref_key_exists("foobar")
        self.assertIsNone(returned_key)
    
    def test_get_ref_type_id_by_name_returns_None_if_no_such_ref_type(self):
        returned_id = self._ref_repository.get_ref_type_id_by_name("foo")
        self.assertIsNone(returned_id)

    def test_get_ref_type_name_by_id_returns_correct_name(self):
        expected_names = {
            1: "book",
            2: "article",
            3: "misc",
            4: "phdthesis",
            5: "incollection"
        }

        for id in range(1,len(expected_names)+1):
            returned_name = self._ref_repository.get_ref_type_name_by_id(id)
            self.assertEqual(returned_name, expected_names[id])

    def test_get_ref_type_name_by_id_returns_None_if_no_such_id_exists(self):
        returned_name = self._ref_repository.get_ref_type_name_by_id(100)
        self.assertIsNone(returned_name)

    def test_get_field_types_by_type_name_book_returns_correct_fields(self):
        field_list = self._ref_repository.get_field_types_by_type_name("book")

        correct_fields ={
            "author": 1,
            "editor": 1,
            "publisher": 1,
            "title": 1,
            "year": 1,
            "address": 0,
            "edition": 0,
            "month": 0,
            "note": 0,
            "number": 0,
            "series": 0,
            "volume": 0}
        

        self.assertEqual(field_list, correct_fields)
