import unittest
from unittest.mock import patch
from services.bibtex_service import (
    create_bibdatabase,
    print_in_bibtex_format
)

class TestBibtexService(unittest.TestCase):
    def setUp(self):
        self._ref_list = [
            {
                "id": 1,
                "ref_key": "Auth1979",
                "type_id": 1,
                "author": "Annie Author",
                "publisher": "Publishing Ltd",
                "title": "The Ultimate Book",
                "year": "1979",
                "edition": "Second",
                "month": "7"
            },
            {
                "id": 2,
                "ref_key": "Misc2021",
                "type_id": 3,
                "author": "Mike Miscellaneous",
                "howpublished": "Blog",
                "title": "A Miscellaneous Blog Post",
                "year": "2021"
            },
            {
                "id": 6,
                "ref_key": "Journ2022",
                "type_id": 2,
                "author": "Jennie Journalist",
                "journal": "Communications of the ACM",
                "title": "AI Explained",
                "year": "2022",
                "month": "12",
                "number": "12",
                "pages": "34--45",
                "volume": "6"
            }
        ]


    def test_create_bibdatabase_returns_bibdatabase_with_correct_content(self):
        bib_db = create_bibdatabase(self._ref_list)

        self.assertEqual(len(bib_db.entries), 3)
        for ref in self._ref_list:
            bib_db_entry = bib_db.entries_dict[ref["ref_key"]]
            self.assertEqual(ref["ref_key"], bib_db_entry["ID"])
            self.assertEqual(ref["author"], bib_db_entry["author"])
            self.assertNotIn("ref_key", bib_db_entry)
            self.assertIn(bib_db_entry["ENTRYTYPE"], "book|misc|article")
    
    @patch('builtins.print')
    def test_print_in_bibtex_format_prints_a_correctly_formatted_list(self, mock_print):
        print_in_bibtex_format(self._ref_list)
        mock_print.assert_called_with(
                "@book{Auth1979,\n"
                + " author = {Annie Author},\n" 
                + " edition = {Second},\n"
                + " month = {7},\n"
                + " publisher = {Publishing Ltd},\n"
                + " title = {The Ultimate Book},\n"
                + " year = {1979}\n}\n"
                + "\n"
                + "@article{Journ2022,\n"
                + " author = {Jennie Journalist},\n"
                + " journal = {Communications of the ACM},\n"
                + " month = {12},\n"
                + " number = {12},\n"
                + " pages = {34--45},\n"
                + " title = {AI Explained},\n"
                + " volume = {6},\n"
                + " year = {2022}\n}\n"
                + "\n"
                + "@misc{Misc2021,\n"
                + " author = {Mike Miscellaneous},\n"
                + " howpublished = {Blog},\n"
                + " title = {A Miscellaneous Blog Post},\n"
                + " year = {2021}\n}\n"
        )
