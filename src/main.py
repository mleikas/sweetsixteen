from UI.ui import UI
from repositories.reference_repository import (
    reference_repository as default_reference_repository
)

ui = UI()
ui.query()

"""
while True:
    print("\n(1) Add ref type")
    print("(2) Get available reference types")          
    print("(3) Add book")
    print("(4) Show all references in database\n")
    cmd = int(input("Command: "))

    if cmd == 1:
        name = input("Reference type name: ")
        new_ref_id = default_reference_repository.add_ref_type(name)
        if new_ref_id:
            print(f"\nAdded reference type: {name}")
        else:
            print(f"\n{name} already exists!")

    if cmd == 2:
        ref_types = default_reference_repository.get_ref_type_names()
        for type in ref_types:
            print(type)

    if cmd == 3:
        mock_book = {
            "author": "Aku Ankka",
            "editor": "",
            "title": "Akun seikkailut",
            "year": 2000,
            "publisher": "Änkkälinnä publishing"
        }
        print("Adding mock book to database")
        default_reference_repository.add_reference(mock_book)   

    if cmd == 4:
        all_references = default_reference_repository.get_all()
        print("\n*** References in database ***")
        for reference in all_references:
            for key, value in reference.items():
                print(f"{key}: {value}")
            print("---")
"""""