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

def write_bibtex_file(save_as="bibtex", id_list=None):
    if id_list:
        all_refs = ref_repo.get_all_references_with_entries()
        ref_list = []
        for reference in all_refs:
            if str(reference["id"]) in id_list:
                ref_list.append(reference)
    else:
        ref_list = ref_repo.get_all_references_with_entries()

    if len(ref_list) > 0:
        bib_db = create_bibdatabase(ref_list)
        dir_path = make_sure_dir_exists("bibtex_files")
        file_name = save_as + ".bib"
        with open(os.path.join(dir_path, file_name), "w", encoding="UTF-8") as bibtex_file:
            dump(bib_db, bibtex_file)
        return file_name
    return None

def make_sure_dir_exists(dir_name:str):
    curr_dir = os.path.dirname(__file__)
    dir_path = os.path.join(curr_dir, "..", "..", dir_name)
    os.makedirs(dir_path, mode=0o777, exist_ok=True)
    return dir_path
