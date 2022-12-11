import unittest
from unittest.mock import Mock
from services.reference_service import ReferenceService, UserInputError, format_references_for_bibtexparser
from repositories.reference_repository import ReferenceRepository
import services.bibtex_service as bib
import os
import tempfile


BOOK_REFERENCE = {
    "key": "BOOK123",
    "type_id": 1,
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
FIELD_TYPES_REFERENCE={
    "address": "0",
    "author": "1",
    "edition": "0",
    "editor": "1",
    "month": "0",
    "note": "0",
    "number": "0",
    "publisher": "1",
    "series": "0?",
    "title": "1",
    "volume": "0",
    "year": "1",
    "author_firstname": "1",
    "author_lastname": "1"
}


class cursorMock():
    def fetchone(self):
        return {"id": "fetchone called"}

    def fetchall(self):
        return [{"id": "fetchall called"}]

    def execute(self, query: str, params: dict):
        return f"Execute called with {query} and params {params}"

class cursorMock2():
    def fetchone(self):
        return {"id": "fetchone called"}

    def fetchall(self):
        return [{"id": "fetchall called"}]

    def execute(self, query: str):
        return f"Execute called with {query}"

class TestValidation(unittest.TestCase):
    def setUp(self):
        self.connection_mock = Mock()
        self.cursor_mock = cursorMock()
        self.connection_mock.configure_mock(
            **{"cursor.return_value": self.cursor_mock})

        self.repository_mock = Mock(
            wraps=ReferenceRepository(self.connection_mock))
        self.service = ReferenceService(self.repository_mock)
        '''self.format=format_references_for_bibtexparser()'''
        self.connection_mock2 = Mock()
        self.cursor_mock2 = cursorMock2()
        self.connection_mock2.configure_mock(
            **{"cursor.return_value": self.cursor_mock2})

        self.repository_mock2 = Mock(
            wraps2=ReferenceRepository(self.connection_mock2))
        self.service2 = ReferenceService(self.repository_mock2)
        

    def test_adding_reference(self):
        self.repository_mock.add_reference.return_value = "BOOK123"
        self.service.add_reference(BOOK_REFERENCE, "book")
        self.repository_mock.add_reference.assert_called_with(
            BOOK_REFERENCE, "book")
        self.repository_mock.add_reference_entries.assert_called_with(
            BOOK_REFERENCE, "BOOK123")
    
    def test_check_ref_key_exists(self):
        self.repository_mock.add_reference.return_value='BOOK123'
        self.repository_mock.check_ref_key_exists.return_value='BOOK123'
        self.service.check_reference_key_exists('BOOK1234')
        self.repository_mock.check_ref_key_exists.assert_called_with("BOOK1234")

    def test_get_ref_keys(self):
        self.repository_mock.get_reference_entries.return_value='1'
        self.service.get_ref_keys('0')
        self.repository_mock.get_reference_entries.assert_called_with("0")
    
    def test_get_fields_by_type_name(self):
        self.repository_mock.get_field_types_by_type_name.return_value='book'
        self.service.get_fields_by_type_name('misc')
        self.repository_mock.get_field_types_by_type_name.assert_called_with('misc')

    def test_get_ref_type_names(self):
        self.service2.get_reference_type_names()
        self.repository_mock2.get_ref_type_names.assert_called()

    def test_delete_reference(self):
        self.repository_mock.delete_reference.return_value = "BOOK123"
        self.service.delete_reference('book')
        self.repository_mock.delete_reference.assert_called_with("book")

    '''def test_get_all_references(self):
        self.service2.get_all_references()
        self.format_ref.assert_called()'''

    def test_get_all_references_with_id(self):
        self.service2.get_all_references_with_id()
        self.repository_mock2.get_all_references_with_entries.assert_called()
    
    def test_get_reference_entries(self):
        self.service2.get_reference_entries()
        self.repository_mock2.get_reference_entries.assert_called()
    
    def test_if_empty(self):
        with self.assertRaises(UserInputError, msg="Field required!"):
            self.service.check_if_empty('')
    
    def test_if_not_empty(self):
        self.assertEqual(self.service2.check_if_empty('a'), None)
    
    def test_format_references_for_bibtexparser(self):

        test_cases = [
            {
                "input": [
                    {
                        "id": "1",
                        "ref_key": "key1",
                        "type_id": "book",
                        "some_field": "some value",
                        "other_field": None,
                    },
                    {
                        "id": "2",
                        "ref_key": "key2",
                        "type_id": "article",
                        "some_field": "another value",
                        "other_field": "",
                    },
                ],
                "expected_output": [
                    {
                        "some_field": "some value",
                        "ID": "key1",

                    },
                    {
                        "some_field": "another value",
                        "ID": "key2",
                    },
                ],
            },

        ]

        for test_case in test_cases:
            inputs = test_case["input"]
            expected_output = test_case["expected_output"]
            self.assertEqual(
                format_references_for_bibtexparser(inputs),
                expected_output,
                f"Failed for input: {inputs}",
            )
class TestBibtexValidation(unittest.TestCase):
    def setUp(self):
        self.ref_list = [
        {"ref_key":'wasd', "type_id": 2,"id": 1, "entry_type": "article", "fields": {"title": "Test Article"}},
        {"ref_key": "asdw", "type_id":1, "id": 2, "entry_type": "book", "fields": {"title": "Test Book"}},
        ]

    def test_create_bibdatabase(self):
        bib_db = bib.create_bibdatabase(self.ref_list)

        self.assertIsInstance(bib_db, bib.bibdatabase.BibDatabase)
        self.assertEqual(bib_db.entries, self.ref_list)
    
    '''def test_print_in_bibtex_format(self):'''

    '''def test_write_bibtex_file(self):'''

    def test_make_sure_dir_exists(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            dir_path = bib.make_sure_dir_exists(os.path.join(temp_dir, "test_dir"))

            self.assertEqual(dir_path, os.path.join(temp_dir, "test_dir"))

            self.assertTrue(os.path.isdir(dir_path))


