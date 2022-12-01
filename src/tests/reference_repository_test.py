import unittest
from utils.initialize_test_database import initialize_test_database
from repositories.reference_repository import test_reference_repository as ref_repository


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        # initilizes the database and inserts two references into the database
        initialize_test_database()
        self._ref_repository = ref_repository
        self._ref_repository.add_reference({"key": "BOOK123", "type_id": 1})
        self._ref_repository.add_reference({"key": "BOOK124", "type_id": 1})

    def test_get_all_references_from_database(self):
        references = self._ref_repository.get_all()

        self.assertEqual(references[0]["ref_key"], "BOOK123")
        self.assertEqual(references[1]["ref_key"], "BOOK124")

    def test_adding_book_reference_with_valid_data_adds_book_to_database(self):
        new_book = {
            "key": "auth2022ABBT",
            "type_id": 1
        }

        self._ref_repository.add_reference(new_book)

        ref_list = self._ref_repository.get_all()
        self.assertEqual(len(ref_list), 3)

    def test_adding_book_entries(self):
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
            "year": "2022",
            "author_firstname": "Authori",
            "author_lastname": "Authorinen"
        }

        self._ref_repository.add_reference_entries(book_entries, 1)
        result = self._ref_repository.get_reference_entries(1)

        self.assertEqual(result["address"], "Osoite123")
        self.assertDictEqual(book_entries, result)

    def test_check_for_existing_cite_key_returns_cite_key_if_key_exists(self):
        returned_key = self._ref_repository.check_ref_key_exists("BOOK123")
        self.assertEqual(returned_key, "BOOK123")

    def test_check_for_existing_cite_key_returns_None_if_key_does_not_exist(self):
        returned_key = self._ref_repository.check_ref_key_exists("foobar")
        self.assertIsNone(returned_key)
