import unittest
from unittest.mock import ANY, patch
from services.bibtex_service import (
    create_bibdatabase,
    print_in_bibtex_format,
    write_bibtex_file,
    check_if_selected_refs_exist
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

    @patch('services.bibtex_service.ref_repo.get_all_references_with_entries')
    def test_write_bibtext_file_with_no_id_list_calls_get_all_references_from_repo(self, mock_get_all_refs):
        mock_get_all_refs.return_value = self._ref_list
        write_bibtex_file("my_references")
        mock_get_all_refs.assert_called_once()

  
    @patch('builtins.open')
    @patch('services.bibtex_service.ref_repo.get_all_references_with_entries')
    def test_write_bibtex_file_calls_open_with_correct_file_name_and_returns_it(self, mock_repo, mock_open):
        mock_repo.return_value = self._ref_list   

        class PathWithDirAndFile(str):
            def __eq__(self, other):
                return "bibtex_files/my_references.bib" in other
        
        returned_name = write_bibtex_file("my_references")
        
        mock_open.assert_called_with(PathWithDirAndFile(mock_open.path), "w", encoding='UTF-8')
        self.assertEqual(returned_name, "my_references.bib")

    @patch('builtins.open')
    @patch('services.bibtex_service.ref_repo.get_all_references_with_entries')
    def test_write_bibtex_file_calls_open_with_default_file_name_if_none_is_given(self, mock_repo, mock_open):
        mock_repo.return_value = self._ref_list   

        class PathWithDirAndFile(str):
            def __eq__(self, other):
                return "bibtex_files/bibtex.bib" in other
        
        returned_name = write_bibtex_file()
        
        mock_open.assert_called_with(PathWithDirAndFile(mock_open.path), "w", encoding='UTF-8')
        self.assertEqual(returned_name, "bibtex.bib")

    @patch('services.bibtex_service.ref_repo.get_all_references_with_entries')
    def test_write_bibtex_file_returns_None_if_there_are_no_references_to_write(self, mock_repo):
        mock_repo.return_value = []

        returned_value = write_bibtex_file()
        self.assertIsNone(returned_value)

    @patch('builtins.open')
    @patch('services.bibtex_service.ref_repo.get_all_references_with_entries')
    def test_write_bibtex_file_calls_open_and_returns_file_name_if_refs_in_id_list_exist(self, mock_repo, mock_open):
        mock_repo.return_value = self._ref_list
        returned_value = write_bibtex_file("my_references", ["1", "6"])

        self.assertEqual(returned_value, "my_references.bib")
        mock_open.assert_called_with(ANY, "w", encoding='UTF-8')

    @patch('builtins.open')
    @patch('services.bibtex_service.ref_repo.get_all_references_with_entries')
    def test_write_bibtex_file_does_not_call_open_and_returns_None_if_refs_in_id_list_do_not_exist(self, mock_repo, mock_open):
        mock_repo.return_value = []
        returned_value = write_bibtex_file("my_references", ["1", "6"])

        self.assertEqual(returned_value, None)
        assert not mock_open.called

    @patch('services.bibtex_service.ref_repo.get_all_references_with_entries')
    def test_check_if_selected_refs_exist_returns_False_if_id_in_given_list_does_not_match(self, mock_repo):
        mock_repo.return_value = self._ref_list

        returned_value = check_if_selected_refs_exist(["1", "20"])
        self.assertEqual(returned_value, False)

    @patch('services.bibtex_service.ref_repo.get_all_references_with_entries')
    def test_check_if_selected_refs_exist_returns_True_if_all_ids_in_given_list_match(self, mock_repo):
        mock_repo.return_value = self._ref_list

        returned_value = check_if_selected_refs_exist(["1", "2", "6"])
        self.assertEqual(returned_value, True)
 