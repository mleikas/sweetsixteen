
from services.reference_service import ReferenceService

"""
from repositories.reference_repository import (
    reference_repository as default_reference_repository
)
"""

class UI:

    def __init__(self):
        self.ref_service = ReferenceService()

    def query(self):

        while True:
            print("\n(1) Add reference type")
            print("(2) Get available reference types")
            print("(3) Add book")
            print("(4) Show all references in database\n")
            print("(Other) End program\n")
            cmd = input("Command: ")

            if cmd == "1":
                name = input("Reference type name: ")
                new_ref_id = self.ref_service.add_reference_type(name)
                if new_ref_id:
                    print(f"\nAdded reference type: {name}")
                else:
                    print(f"\n{name} already exists!")

            if cmd == "2":
                ref_types = self.ref_service.get_reference_type_names()
                for type in ref_types:
                    print(type)

            if cmd == "3":
                book_dict = self.ref_service.add_book()
                self.ref_service.submit_book_reference(book_dict)

            if cmd == "4":
                all_references = self.ref_service.get_all_references()
                print("\n*** References in database ***")
                for reference in all_references:
                    for key, value in reference.items():
                        print(f"{key}: {value}")
                    print("---")
            
            else:
                break
    """
    def book(self):
        key=''
        author_or_editor=0
        author=''
        editor=''
        title=''
        publisher=''
        year=''
        while key=='':
            key=input('Searching key: ')
        while int(author_or_editor) != 1 and int(author_or_editor) != 2:
            author_or_editor=input('Press 1 if your book has an author and 2 if an editor: ')
        if author_or_editor=='1':
            while author=='':
                author=input("Book's author: ")
        elif author_or_editor=='2':
            while editor=='':
                editor=input("Book's editor: ")
        while title=='':
            title=input("Book's title: ")
        while publisher=='':
            publisher=input("Book's publisher: ")
        while year=='':
            year=input("Publishing year: ")
        volume=input("Book's volume/number(optional): ")
        series=input("Book's series(optional): ")
        address=input("Book's address(optional): ")
        edition=input("Book's edition(optional): ")
        month=input("Publishing month(optional): ")
        note=input("Book's note(optional): ")
        book_dict={
            'key':key,
            'author': author,
            'editor': editor,
            'title': title,
            'publisher':publisher,
            'year':year,
            'volume':volume,
            'series':series,
            'address':address,
            'edition':edition,
            'month':month,
            'note':note,
        }
        return book_dict
    """
