from bibtexparser import bibdatabase, dumps
from repositories.reference_repository import reference_repository as rr
from services.reference_service import organise_references_for_output

def parse():
    database = bibdatabase.BibDatabase()
    references = organise_references_for_output(rr.get_all_references_with_entries())
    for reference in references:
        database.entries.append(reference)
    print(dumps(database))
