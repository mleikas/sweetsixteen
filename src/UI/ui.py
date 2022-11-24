def query():
    type=input("Reference's type: ")
    if type=='book':
        return book()

def book():
    while key=='':
        key=input('Searching key: ')
    while author_or_editor!='1' or author_or_editor!='2':
        author_or_editor=input('Press 1 if your book has an author and 2 if an editor: ')
    if author_or_editor=='1':
        while author=='':
            author=input("Book's author: ")
    elif author_or_editor=='2':
        while editor=='':
            editor=input("Book's editor: ")
    while title=='':
        title=input("Book's title: ")
    while publisher=='':
        publisher=input("Book's publisher: ")
    while year=='':
        year=input("Publishing year: ")
    volume=input("Book's volume/number(optional): ")
    series=input("Book's series(optional): ")
    address=input("Book's address(optional): ")
    edition=input("Book's edition(optional): ")
    month=input("Publishing month(optional): ")
    note=input("Book's note(optional): ")
    book_dict={
        'key':key,
        'author': author,
        'editor': editor,
        'title': title,
        'publisher':publisher,
        'year':year,
        'volume':volume,
        'series':series,
        'address':address,
        'edition':edition,
        'month':month,
        'note':note,
    }
    return book_dict
