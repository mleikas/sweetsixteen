class UserInputError(Exception):
    pass

class ReferenceService():
    def __init__(self):
        pass

    def validate_book_input(self, book:dict):
        if book["author"] == "" and book["editor"] == "":
            raise UserInputError("Author or editor required!")
        if book["title"] == "":
            raise UserInputError("Title required!")
        if book["publisher"] == "":
            raise UserInputError("Publisher required!")
        if book["year"] == "":
            raise UserInputError("Year required!")

reference_service = ReferenceService()