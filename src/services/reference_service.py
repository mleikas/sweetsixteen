
from repositories.reference_repository import (
    reference_repository as default_reference_repository
)


class UserInputError(Exception):
    pass

class ReferenceService():
    def __init__(self):
        pass

    def add_book(self):
        key = ''
        author_or_editor = 0
        author = ''
        editor = ''
        title = ''
        publisher = ''
        year = ''
        while key == '':
            key = input('Searching key: ')
        while int(author_or_editor) != 1 and int(author_or_editor) != 2:
            author_or_editor = input('Press 1 if your book has an author and 2 if an editor: ')
        if author_or_editor == '1':
            while author == '':
                author = input("Book's author: ")
        elif author_or_editor == '2':
            while editor == '':
                editor = input("Book's editor: ")
        while title == '':
            title = input("Book's title: ")
        while publisher == '':
            publisher = input("Book's publisher: ")
        while year == '':
            year = input("Publishing year: ")
        volume = input("Book's volume/number(optional): ")
        series = input("Book's series(optional): ")
        address = input("Book's address(optional): ")
        edition = input("Book's edition(optional): ")
        month = input("Publishing month(optional): ")
        note = input("Book's note(optional): ")
        book_dict = {
            'key': key,
            'author': author,
            'editor': editor,
            'title': title,
            'publisher': publisher,
            'year': year,
            'volume': volume,
            'series': series,
            'address': address,
            'edition': edition,
            'month': month,
            'note': note,
        }
        return book_dict

    def add_reference_type(self, name):
        return default_reference_repository.add_ref_type(name)

    def get_reference_type_names(self):
        return default_reference_repository.get_ref_type_names()

    def add_reference(self, book_dict):
        return default_reference_repository.add_reference(book_dict)

    def get_all_references(self):
        return default_reference_repository.get_all()

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