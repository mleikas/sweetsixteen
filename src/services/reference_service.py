

from repositories.reference_repository import reference_repository as rr


class UserInputError(Exception):
    pass

class ReferenceService():
    def __init__(self):
        pass

    def add_reference_type(self, name):
        return rr.add_ref_type(name)

    def check_reference_key_exists(self, key_candidate):
        return rr.check_ref_key_exists(key_candidate)

    def get_reference_type_names(self):
        return rr.get_ref_type_names()

    def add_reference(self, book):
        return rr.add_reference(book)

    def get_all_references(self):
        return rr.get_all()

    def submit_book_reference(self, book:dict):
        rr.add_reference(book)

    def check_if_empty(self, input):
        if input == "":
            raise UserInputError("Field required!")

    def validate_book_input(self, book:dict):
        """checks for missing but mandatory info as well as input length
        """
        if book["author"] == "" and book["editor"] == "":
            raise UserInputError("Author or editor required!")
        if len(book["author"]) > 100 or len(book["editor"]) > 100:
            raise UserInputError("Author or editor name too long.")
        if book["title"] == "":
            raise UserInputError("Title required!")
        if len(book["title"]) > 200:
            raise UserInputError("Title too long")
        if book["publisher"] == "":
            raise UserInputError("Publisher required!")
        if book["year"] == "":
            raise UserInputError("Year required!")

reference_service = ReferenceService()