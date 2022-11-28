

from repositories.reference_repository import reference_repository as rr


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
            key_candidate = input('Citation key: ')
            if not rr.check_ref_key_exists(key_candidate):
                key = key_candidate
            else:
                print("That citation key is already in use. Choose another one.")
        while author_or_editor not in ['1', '2']:
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
        return rr.add_ref_type(name)

    def get_reference_type_names(self):
        return rr.get_ref_type_names()

    def add_reference(self, book):
        return rr.add_reference(book)

    def get_all_references(self):
        return rr.get_all()

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