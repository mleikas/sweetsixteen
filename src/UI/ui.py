import os
from services.reference_service import ReferenceService
from services.parser import parse

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

            if cmd == "2":
                key=''
                while key not in ['book', 'misc', 'article', 'phdthesis', 'incollection']:
                    key = input("Which reference type? (book/misc/article/phdthesis/incollection): ")
                ref_dict = self.ref_query(key)
                self.ref_service.validate_book_input(ref_dict)
                self.ref_service.add_reference(ref_dict, key)


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

            next_input()
    
    def fields(self, type_name):
        fields=self.ref_service.get_fields_by_type_name(type_name)
        return fields



    def ref_query(self, type_name):
        fields=self.fields(type_name)
        author_or_editor=''
        ref_dict={}
        key=input(self.ui_library.questions_dict['key'] + '(required): ')
        while self.ref_service.check_reference_key_exists(key)!=None:
            key=input(self.ui_library.questions_dict['key'] + '(required): ')
        ref_dict['key']=key
        if 'author_firstname' in fields.keys() and 'editor' in fields.keys():
            while author_or_editor not in ['1', '2']:
                author_or_editor = input('Press 1 if your book has an author and 2 if an editor: ')
            if author_or_editor == '1':
                fields.pop('editor')
                ref_dict['editor']=''
            elif author_or_editor == '2':
                fields.pop('author_firstname')
                fields.pop('author_lastname')
                ref_dict['author_firstname']=''
                ref_dict['author_lastname']=''

        for field, req in fields.items():
                
            if req==1:
                answer=''
                while answer=='':
                    answer=input(self.ui_library.questions_dict[field] + '(required): ')

            else:
                answer=input(self.ui_library.questions_dict[field] + '(optional): ')
            if field == 'year' and answer.isnumeric()==False:
                while answer.isnumeric()==False:
                    answer=input(self.ui_library.questions_dict[field] + '(only numbers): ')

            ref_dict[field]=answer
        return ref_dict
       
class UIData:
    def __init__(self) -> None:
        self.questions_dict={
            'key':'Citation key ',
            'author': 'Author ',
            'author_firstname': 'First name ',
            'author_lastname': 'Last name',
            'editor':('Last name ', 'First name '),
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

        
        
        
        
        
        
        
        
        
        '''if key=="book":
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
            return keys'''

def next_input():
    print()
    input("Press enter to continue...")
