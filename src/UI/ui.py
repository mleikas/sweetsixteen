from services.reference_service import ReferenceService
from services.parser import run as parse
from UI.UILibrary import UILibrary

class UI:

    def __init__(self):
        self.ref_service = ReferenceService()
        self.ui_library=UILibrary()

    def query(self):

        while True:
            print("\n(1) Get available reference types")
            print("(2) Add reference")
            print("(3) Show all references in database")
            print("(4) Show references in bibtex format")
            print("(5) Delete reference from database\n")
            print("(Other) End program\n")
            cmd = input("Command: ")

            if cmd == "1":
                ref_types = self.ref_service.get_reference_type_names()
                for r_type in ref_types:
                    print(r_type)

            if cmd == "2":
                ''' book_dict = self.book()
                    self.ref_service.validate_book_input(book_dict)
                    self.ref_service.submit_book_reference(book_dict) '''
                key=''
                while key not in ['book', 'misc', 'article', 'phdthesis', 'incollection']:
                    key = input("Which reference type? (book/misc/article/phdthesis/incollection): ")
                ref_dict = self.ref_query(key)
                self.ref_service.validate_book_input(ref_dict)
                self.ref_service.submit_book_reference(ref_dict)

            if cmd == "3":
                all_references = self.ref_service.get_all_references()
                print("\n*** References in database ***")
                for reference in all_references:
                    for key, value in reference.items():
                        print(f"{key}: {value}")
                    print("---")

            if cmd == "4":
                parse()
            
            if cmd == "5":
                ref_key = input("Enter citation key of reference to delete: ")
                # TODO: verify that cite key exists
                # Show e.g. author, title, year and ask user to verify
                self.ref_service.delete_reference(ref_key)
                print("Reference was removed from database.")

            if cmd not in ["1", "2", "3", "4", "5"]:
                break

    def ref_query(self, key):
        keys=self.ui_library.keys(key)
        author_or_editor=''
        ref_dict={}
        while author_or_editor not in ['1', '2']:
            author_or_editor = input('Press 1 if your book has an author and 2 if an editor: ')
        if author_or_editor == '1':
            keys.remove('editor')
            ref_dict['editor']=''
        elif author_or_editor == '2':
            keys.remove('author')
            ref_dict['author']=''

        for i in keys:
            if i in ['author', 'editor', 'year', 'title', 'publisher', 'year', 'key']:
                answer=''
                while answer=='':
                    answer=input(self.ui_library.questions_dict[i])

            else:
                answer=input(self.ui_library.questions_dict[i])
            ref_dict[i]=answer
        return ref_dict
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''key = ''
        author_or_editor = 0
        author = ''
        editor = ''
        title = ''
        publisher = ''
        year = ''
        while key == '':
            key_candidate = input('Citation key: ')
            if not self.ref_service.check_reference_key_exists(key_candidate):
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
        return book_dict'''
