import os
from services.reference_service import ReferenceService
from services.parser import parse


class UI:

    def __init__(self):
        self.ref_service = ReferenceService()
        self.ui_library = UIData()
        self.reference_types = self.ref_service.get_reference_type_names()
        self.commands = {
            "1": self.print_type_names,
            "2": self.add_reference,
            "3": self.print_reference_list,
            "4": parse,
            "5": self.delete_reference
        }

    def print_menu(self):
        print("\n(1) Get available reference types")
        print("(2) Add reference")
        print("(3) Show all references in database")
        print("(4) Show references in bibtex format")
        print("(5) Delete reference from database\n")
        print("(Other) End program\n")

    def print_type_names(self):
        ref_types = self.ref_service.get_reference_type_names()
        for r_type in ref_types:
            print(r_type)

    def add_reference(self):
        key = ''
        while key not in self.reference_types:
            key = input(
                f"Which reference type {'/'.join(self.reference_types)} ?: "
            )
        ref_dict = self.ref_query(key)
        self.ref_service.add_reference(ref_dict, key)

    def print_reference_list(self):
        all_references = self.ref_service.get_all_references()
        print("\n*** References in database ***")
        for reference in all_references:
            for key, value in reference.items():
                print(f"{key}: {value}")
            print("---")

    def delete_reference(self):
        ref_key = input("Enter citation key of reference to delete: ")
        if self.ref_service.check_reference_key_exists(ref_key):
            self.ref_service.delete_reference(ref_key)
            print("Reference was deleted from database.")
        else:
            print("No reference with such citation key.")

    def query(self):

        while True:
            os.system('clear')
            self.print_menu()
            cmd = input("Command: ")

            if cmd not in self.commands.keys():
                break

            self.commands[cmd]()
            next_input()

    def fields(self, type_name):
        fields = self.ref_service.get_fields_by_type_name(type_name)
        return fields

    def ref_query(self, type_name):
        fields = self.fields(type_name)
        author_or_editor = ''
        ref_dict = {}
        key = input(self.ui_library.questions_dict['key'] + '(required): ')
        while self.ref_service.check_reference_key_exists(key) is not None:
            key = input(self.ui_library.questions_dict['key'] + '(required): ')
        ref_dict['key'] = key
        if 'author' in fields.keys() and 'editor' in fields.keys():
            while author_or_editor not in ['1', '2']:
                author_or_editor = input(
                    'Press 1 if your book has an author and 2 if an editor: ')
            if author_or_editor == '1':
                fields.pop('editor')
                ref_dict['editor'] = ''
            elif author_or_editor == '2':
                fields.pop('author')
                fields.pop('author_firstname')
                fields.pop('author_lastname')
                ref_dict['author'] = ''
                ref_dict['author_firstname'] = ''
                ref_dict['author_lastname'] = ''

        for field, req in fields.items():
            if req == 1:
                answer = ''
                while answer == '':
                    answer = input(
                        self.ui_library.questions_dict[field] + '(required): ')
            else:
                answer = input(
                    self.ui_library.questions_dict[field] + '(optional): ')

            if field == 'year' and answer.isnumeric() is False and answer != '':
                while answer.isnumeric() is False:
                    answer = input(
                        self.ui_library.questions_dict[field] + '(only numbers): ')

            ref_dict[field] = answer
        return ref_dict


class UIData:
    def __init__(self) -> None:
        self.questions_dict = {
            'key': 'Citation key ',
            'author': 'Author ',
            'author_firstname': 'First name ',
            'author_lastname': 'Last name',
            'editor': 'Editor ',
            'title': 'Title ',
            'publisher': 'Publisher ',
            'year': 'Year ',
            'journal': 'Journal ',
            'volume': 'Volume ',
            'series': 'Series ',
            'address': 'Address ',
            'edition': 'Edition ',
            'month': 'Month ',
            'chapter': 'Chapter ',
            'note': 'Note ',
            'number': 'Number ',
            'type': 'Type ',
            'school': 'School ',
            'booktitle': "Book title ",
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
