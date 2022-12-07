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
        # Write only the references in the list to file.
        # Functionality could also be implemented
        # by providing a list of indices
        # that could be used for filtering
        # when creating the bibdatabase before saving.
        pass
    else:
        ref_list = ref_repo.get_all_references_with_entries()
        bib_db = create_bibdatabase(ref_list)
        with open(os.path.join('bibtex_files', 'bibtex.bib'), 'w', encoding='UTF-8') as bibtex_file:
            dump(bib_db, bibtex_file)
