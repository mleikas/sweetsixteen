import unittest
from unittest.mock import Mock
from services.reference_service import ReferenceService, UserInputError
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

    def test_adding_reference(self):
        self.repository_mock.add_reference.return_value = "BOOK123"
        self.service.add_reference(BOOK_REFERENCE, "book")
        self.repository_mock.add_reference.assert_called_with(
            BOOK_REFERENCE, "book")
        self.repository_mock.add_reference_entries.assert_called_with(
            BOOK_REFERENCE, "BOOK123")
