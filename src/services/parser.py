from repositories.reference_repository import reference_repository as rr
from bibtexparser import bibdatabase, dump, dumps



def parse():
    database = bibdatabase.BibDatabase()
    all_references = rr.get_all()
    for reference in all_references:
        del reference["id"]
        reference["ID"] = reference.pop("ref_key")
        reference["ENTRYTYPE"] = reference.pop("type_id")
        if reference["ENTRYTYPE"] == 1:
            reference["ENTRYTYPE"] = "book"
        if reference["ENTRYTYPE"] == 2:
            reference["ENTRYTYPE"] = "article"


        database.entries.append(reference)

    print(dumps(database))