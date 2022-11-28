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
