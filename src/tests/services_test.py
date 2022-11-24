import unittest
from services.reference_service import reference_service, UserInputError

class TestValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.rs = reference_service

    def test_empty_author(self):
        mock_book = {
            "author": "",
            "editor": "",
            "title": "Akun seikkailut",
            "year": 2000,
            "publisher": "Änkkälinnä publishing"
        }
        self.assertRaises(UserInputError, lambda: self.rs.validate_book_input(mock_book))

    def test_empty_title(self):
        mock_book = {
            "author": "Aku Ankka",
            "editor": "",
            "title": "",
            "year": 2000,
            "publisher": "Änkkälinnä publishing"
        }
        self.assertRaises(UserInputError, lambda: self.rs.validate_book_input(mock_book))

    def test_empty_year(self):
        mock_book = {
            "author": "Aku Ankka",
            "editor": "",
            "title": "Akun seikkailut",
            "year": "",
            "publisher": "Änkkälinnä publishing"
        }
        self.assertRaises(UserInputError, lambda: self.rs.validate_book_input(mock_book))

    def test_empty_publisher(self):
        mock_book = {
            "author": "Aku Ankka",
            "editor": "",
            "title": "Akun seikkailut",
            "year": 2000,
            "publisher": ""
        }
        self.assertRaises(UserInputError, lambda: self.rs.validate_book_input(mock_book))
