import os
from bibtexparser import bibdatabase, dump, dumps
from repositories.reference_repository import reference_repository as ref_repo
from services.reference_service import format_references_for_bibtexparser


def create_bibdatabase(ref_list:list):
    bib_db = bibdatabase.BibDatabase()
    references = format_references_for_bibtexparser(ref_list)
    bib_db.entries = references[:]
    return bib_db

def print_in_bibtex_format(ref_list=None):
    if not ref_list:
        ref_list = ref_repo.get_all_references_with_entries()
    database = create_bibdatabase(ref_list)
    print(dumps(database))


def write_bibtex_file(ref_list=None):
    if ref_list:
        all_refs = ref_repo.get_all_references_with_entries()
        filtered_ref_list = []
        for reference in all_refs:
            if str(reference["id"]) in ref_list:
                filtered_ref_list.append(reference)

        if len(filtered_ref_list) != 0:
            bib_db = create_bibdatabase(filtered_ref_list)
            with open(os.path.join('bibtex_files', 'bibtex_filtered.bib'), 'w', encoding='UTF-8') as bibtex_file:
                dump(bib_db, bibtex_file)
            print("The file 'bibtex_filtered.bib' was saved to the bibtex_files folder")
        else:
            print("No references matching given selections, not creating bibtex file")

    else:
        ref_list = ref_repo.get_all_references_with_entries()
        bib_db = create_bibdatabase(ref_list)
        with open(os.path.join('bibtex_files', 'bibtex.bib'), 'w', encoding='UTF-8') as bibtex_file:
            dump(bib_db, bibtex_file)
