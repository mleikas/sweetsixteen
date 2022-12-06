from repositories.reference_repository import reference_repository as rr
from bibtexparser import bibdatabase, dump, dumps


def filter_empty_values(ref):
    new_ref = {}
    for key in ref:
        if ref[key] != "":
            new_ref[key] = ref[key]

    return new_ref
                

def parse():
    database = bibdatabase.BibDatabase()
    all_references = rr.get_all_references_with_entries()
    for reference in all_references:
        del reference["id"]
        reference["ID"] = reference.pop("ref_key")
        reference["ENTRYTYPE"] = reference.pop("type_id")
        if reference["ENTRYTYPE"] == 1:
            reference["ENTRYTYPE"] = "book"
        if reference["ENTRYTYPE"] == 2:
            reference["ENTRYTYPE"] = "article"
        if reference["ENTRYTYPE"] == 3:
            reference["ENTRYTYPE"] = "misc"
        if reference["ENTRYTYPE"] == 4:
            reference["ENTRYTYPE"] = "phdthesis"
        if reference["ENTRYTYPE"] == 5:
            reference["ENTRYTYPE"] = "incollection"

        reference = filter_empty_values(reference)

        database.entries.append(reference)

    print(dumps(database))