import unittest
from utils.initialize_test_database import initialize_test_database
from repositories.reference_repository import test_reference_repository as ref_repository


class TestReferenceRepository(unittest.TestCase):
    def setUp(self):
        # initilizes the database and inserts two references into the database
        initialize_test_database()
        self._ref_repository = ref_repository

    def test_get_all_references_from_database(self):
        references = self._ref_repository.get_all()

        self.assertEqual(references[0]["ref_key"], "BOOK123")
        self.assertEqual(references[1]["ref_key"], "BOOK124")

    def test_adding_book_reference_with_valid_data_adds_book_to_database(self):
        new_book = {
            "key": "auth2022ABBT",
            "author": "Author, Annie",
            "editor": "",
            "title": "A Brilliant Book Title",
            "publisher": "Publishing Ltd",
            "year": "2022",
            "volume": "",
            "series": "Insightful Books",
            "address": "Helsinki",
            "edition": "",
            "month": "",
            "note": "",
        }

        self._ref_repository.add_reference(new_book)
        
        ref_list = self._ref_repository.get_all()
        self.assertEqual(len(ref_list), 3)
    
    def test_check_for_existing_cite_key_returns_cite_key_if_key_exists(self):
        returned_key = self._ref_repository.check_ref_key_exists("BOOK123")
        self.assertEqual(returned_key, "BOOK123")

    def test_check_for_existing_cite_key_returns_None_if_key_does_not_exist(self):
        returned_key = self._ref_repository.check_ref_key_exists("foobar")
        self.assertIsNone(returned_key)
