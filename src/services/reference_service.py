
from repositories.reference_repository import reference_repository as rr


class UserInputError(Exception):
    pass


class ReferenceService():
    def __init__(self):
        pass

    def check_reference_key_exists(self, key_candidate):
        return rr.check_ref_key_exists(key_candidate)

    def get_reference_type_names(self):
        return rr.get_ref_type_names()

    def add_reference(self, reference):
        rr.add_reference(reference)
        ref_key = rr.check_ref_key_exists(reference["ref_key"])
        return rr.add_reference_entries(reference)

    def delete_reference(self, ref_key: str):
        rr.delete_reference(ref_key)

    def get_all_references(self):
        references = rr.get_all()
        new_references = []
        for ref in references:
            new_ref = {}
            for key in ref:
                if ref[key] != "" and key not in ["id", "type_id"]:
                    new_ref[key] = ref[key]
            new_references.append(new_ref)
        return new_references

    def get_reference_entries(self):
        return rr.get_reference_entries()

    def submit_book_reference(self, book: dict, type_name):
        rr.add_reference(book, type_name)

    def check_if_empty(self, input):
        if input == "":
            raise UserInputError("Field required!")

    def validate_book_input(self, book: dict):
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
