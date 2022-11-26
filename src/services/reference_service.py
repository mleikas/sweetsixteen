from repositories.reference_repository import reference_repository as rr

class UserInputError(Exception):
    pass

class ReferenceService():
    def __init__(self):
        pass

    def submit_book_reference(self, book:dict):
        rr.add_reference(book)

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