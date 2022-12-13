from services.reference_service import reference_service


BOOK = {
    "key": "BOOK1",
    "author": "Alan Casey",
    "publisher": "Hauppauge, New York : Nova Science Publishers, Inc.",
    "title": "Soft computing : developments, methods and applications",
    "year": "2016",
    "note": "Excellent book",
}

ARTICLE = {
    "key": "ARTICLE1",
    "author": "Witold Pedrycz",
    "journal": "Industrial electronic series",
    "title": "Granular computing: analysis and design of intelligent systems",
    "year": "2013",
    "pages": "295",
}

MISC = {
    "key": "MISC1",
    "author": "Association for Computing Machinery",
    "title": "ACM computing surveys (Online)",
    "year": "1971",
}

PHDTHESIS = {
    "key": "PHDTHESIS1",
    "author": "Markku Alho",
    "school": "University of Helsinki",
    "title": "Hybrid plasma modelling in the inner Solar System",
    "year": "2022"
}
INCOLLECTION = {
    "key": "INCOLLECTION1",
    "author": "David Lewis",
    "booktitle": "Science Fiction and Philosophy",
    "publisher": "West Sussex, England : Wiley Blackwell",
    "title": "The Paradoxes of Time Travel",
    "year": "2016",
    "pages": "357--369"
}


if __name__ == "__main__":
    reference_service.add_reference(BOOK, "book")
    reference_service.add_reference(ARTICLE, "article")
    reference_service.add_reference(MISC, "misc")
    reference_service.add_reference(PHDTHESIS, "phdthesis")
    reference_service.add_reference(INCOLLECTION, "incollection")
