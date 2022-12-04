import os
from services.reference_service import ReferenceService
from services.parser import run as parse

class UI:

    def __init__(self):
        self.ref_service = ReferenceService()
        self.ui_library=UIData()

    def query(self):

        while True:
            os.system('clear')
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
                next_input()

            if cmd == "2":
                key=''
                while key not in ['book', 'misc', 'article', 'phdthesis', 'incollection']:
                    key = input("Which reference type? (book/misc/article/phdthesis/incollection): ")
                ref_dict = self.ref_query(key)
                self.ref_service.validate_book_input(ref_dict)
                self.ref_service.submit_book_reference(ref_dict, key)
                next_input()

            if cmd == "3":
                all_references = self.ref_service.get_all_references()
                print("\n*** References in database ***")
                for reference in all_references:
                    for key, value in reference.items():
                        print(f"{key}: {value}")
                    print("---")
                next_input()

            if cmd == "4":
                parse()
                next_input()

            if cmd == "5":
                ref_key = input("Enter citation key of reference to delete: ")
                # TODO: verify that cite key exists
                # Show e.g. author, title, year and ask user to verify
                self.ref_service.delete_reference(ref_key)
                print("Reference was removed from database.")
                next_input()

            if cmd not in ["1", "2", "3", "4", "5", "6"]:
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
            if i == 'author' or i=='editor':
                answer=''
                while answer=='':
                    surname=input(self.ui_library.questions_dict[i][0] + '(required): ')
                    first_name=input(self.ui_library.questions_dict[i][1] + '(required): ')
                    answer=f'{surname}_{first_name}'
            elif i in ['year', 'title', 'publisher', 'year', 'key']:
                answer=''
                while answer=='':
                    answer=input(self.ui_library.questions_dict[i] + '(required): ')

            else:
                answer=input(self.ui_library.questions_dict[i] + '(optional): ')
            ref_dict[i]=answer
        return ref_dict
       
class UIData:
    def __init__(self) -> None:
        self.questions_dict={
            'key':'Citation key ',
            'author':('Surname ', 'First name'),
            'editor':'Editor ',
            'title':'Title ',
            'publisher':'Publisher ',
            'year':'Year ',
            'volume':'Volume ',
            'series':'Series ',
            'address':'Address ',
            'edition':'Edition ',
            'month':'Month ',
            'note':'Note ',
            'number':'Number ',
            'type':'Type ',
            'school':'School ',
            'booktitle':"Book title ",
            'howpublished': 'How published ',
            'pages': 'Pages '
        }

    def keys(self, key):
        if key=="book":
            keys=['key',
            'author',
            'editor',
            'title',
            'publisher',
            'year',
            'volume',
            'series',
            'address',
            'edition',
            'month',
            'note']
            return keys

def next_input():
    print()
    input("Press any key to continue...")
