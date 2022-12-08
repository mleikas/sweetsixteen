from repositories.reference_repository import reference_repository as default_ref_repository


def format_references_for_bibtexparser(references:list):
    formatted_refs = []
    for reference in references:
        del reference["id"]
        reference["ID"] = reference.pop("ref_key")
        type_id = reference.pop("type_id")
        entry_type = default_ref_repository.get_ref_type_name_by_id(type_id)
        reference["ENTRYTYPE"] = entry_type
        no_empties_ref = {}
        for key, value in reference.items():
            if value:
                no_empties_ref[key] = value
        formatted_refs.append(no_empties_ref)
    return formatted_refs


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
        return references

    def get_reference_type_names(self):
        return self.ref_repo.get_ref_type_names()

    def add_reference(self, reference, ref_type):
        ref_id = self.ref_repo.add_reference(reference, ref_type)
        return self.ref_repo.add_reference_entries(reference, ref_id)

    def delete_reference(self, ref_key: str):
        self.ref_repo.delete_reference(ref_key)

    def get_all_references(self):
        references = format_references_for_bibtexparser(
            self.ref_repo.get_all_references_with_entries())
        return references

    def get_reference_entries(self):
        return self.ref_repo.get_reference_entries()

    def check_if_empty(self, entry):
        if entry == "":
            raise UserInputError("Field required!")


reference_service = ReferenceService()
