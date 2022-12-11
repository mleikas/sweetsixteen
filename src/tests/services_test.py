import unittest
from unittest.mock import Mock, call
from services.reference_service import ReferenceService, UserInputError, format_references_for_bibtexparser
from repositories.reference_repository import ReferenceRepository


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

BOOK_REFERENCE_MANY_AUTHORS = {
    "key": "BOOK1234",
    "type_id": 1,
    "address": "",
    "author": ["Author_1", "Author_2", "Author_3"],
    "edition": "",
    "editor": "",
    "month": "",
    "note": "",
    "number": "",
    "publisher": "Sanoma",
    "series": "",
    "title": "Book title",
    "volume": "",
    "year": "2022",
    "author_firstname": "",
    "author_lastname": ""
}

BOOK_REFERENCE_PRUNED_AUTHORS = {
    "key": "BOOK1234",
    "type_id": 1,
    "address": "",
    "author": "Author_3",
    "edition": "",
    "editor": "",
    "month": "",
    "note": "",
    "number": "",
    "publisher": "Sanoma",
    "series": "",
    "title": "Book title",
    "volume": "",
    "year": "2022",
    "author_firstname": "",
    "author_lastname": ""
}

FIELD_TYPES_REFERENCE = {
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

    def test_adding_reference(self):
        self.repository_mock.add_reference.return_value = "BOOK123"
        self.service.add_reference(BOOK_REFERENCE, "book")
        self.repository_mock.add_reference.assert_called_with(
            BOOK_REFERENCE, "book")
        self.repository_mock.add_reference_entries.assert_called_with(
            BOOK_REFERENCE, "BOOK123")

    def test_multiple_authors(self):
        self.repository_mock.add_reference.return_value = "BOOK1234"
        self.service.add_reference(
            BOOK_REFERENCE_MANY_AUTHORS, "book")
        self.repository_mock.add_reference_entries.assert_has_calls(
            [call({"author": "Author_1"}, "BOOK1234"),
             call({"author": "Author_2"}, "BOOK1234"),
             call(BOOK_REFERENCE_PRUNED_AUTHORS, "BOOK1234")],
            any_order=False
        )

    def test_check_ref_key_exists(self):
        self.repository_mock.add_reference.return_value = 'BOOK123'
        self.repository_mock.check_ref_key_exists.return_value = 'BOOK123'
        self.service.check_reference_key_exists('BOOK1234')
        self.repository_mock.check_ref_key_exists.assert_called_with(
            "BOOK1234")

    def test_get_ref_keys(self):
        self.repository_mock.get_reference_entries.return_value = '1'
        self.service.get_ref_keys('0')
        self.repository_mock.get_reference_entries.assert_called_with("0")

    def test_get_fields_by_type_name(self):
        self.repository_mock.get_field_types_by_type_name.return_value = 'book'
        self.service.get_fields_by_type_name('misc')
        self.repository_mock.get_field_types_by_type_name.assert_called_with(
            'misc')

    '''def test_get_ref_type_names(self):
        self.service.get_reference_type_names()
        self.repository_mock.get_ref_type_names.assert_called_with(self)'''

    def test_delete_reference(self):
        self.repository_mock.delete_reference.return_value = "BOOK123"
        self.service.delete_reference('book')
        self.repository_mock.delete_reference.assert_called_with("book")

    '''def test_format_references_for_bibtex_parser(self):
        self.repository_mock.get_ref_type_name_by_id('1')
        self.for'''

    '''def test_get_all_references(self):
        self.repository_mock.get_all_references_with_entries()
        self.service.get_all_references()
        self.repository_mock.get_all_references_with_entries.assert_called()'''
