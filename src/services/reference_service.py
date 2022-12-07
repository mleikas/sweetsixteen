from repositories.reference_repository import reference_repository as default_ref_repository


def organise_references_for_output(references):
    new_references = []
    for reference in references:
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
        new_ref = {}
        for key in reference:
            if reference[key] != "":
                new_ref[key] = reference[key]
        new_references.append(new_ref)
    return new_references


class UserInputError(Exception):
    pass


class ReferenceService():
    def __init__(self, reference_repository=default_ref_repository):
        self.ref_repo = reference_repository

    def check_reference_key_exists(self, key_candidate):
        return self.ref_repo.check_ref_key_exists(key_candidate)

    def get_ref_keys(self, ref_id):
        return self.ref_repo.get_reference_entries(ref_id)

    def get_fields_by_type_name(self, type_name):
        references = self.ref_repo.get_field_types_by_type_name(type_name)
        new_references = {}
        for ref in references:
            new_references[ref['type_name']] = ref["required"]
        return new_references

    def get_reference_type_names(self):
        return self.ref_repo.get_ref_type_names()

    def add_reference(self, reference, ref_type):
        ref_id = self.ref_repo.add_reference(reference, ref_type)
        return self.ref_repo.add_reference_entries(reference, ref_id)

    def delete_reference(self, ref_key: str):
        self.ref_repo.delete_reference(ref_key)

    def get_all_references(self):
        references = organise_references_for_output(
            self.ref_repo.get_all_references_with_entries())
        return references

    def get_reference_entries(self):
        return self.ref_repo.get_reference_entries()

    def submit_book_reference(self, book: dict, type_name):
        self.ref_repo.add_reference(book, type_name)

    def check_if_empty(self, entry):
        if entry == "":
            raise UserInputError("Field required!")


reference_service = ReferenceService()
