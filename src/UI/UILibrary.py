class UILibrary:
    def __init__(self) -> None:
        self.questions_dict={
            'key':'Citation key: ',
            'author':'Author: ',
            'editor':'Editor: ',
            'title':'Title: ',
            'publisher':'Publisher: ',
            'year':'Year: ',
            'volume':'Volume: ',
            'series':'Series: ',
            'address':'Address: ',
            'edition':'Edition: ',
            'month':'Month: ',
            'note':'Note: ',
            'number':'Number: ',
            'type':'Type: ',
            'school':'School: ',
            'booktitle':"Book title: ",
            'howpublished': 'How published: ',
            'pages': 'Pages: '
        }


    def input_value(self, value):
        # input a value into ui
        user_input=input(value)
        return user_input

    def reference_count_should_be(self, value):
        self.input_value(4)
        # check that book IDs don't ecceed 1
        pass

    def keys(self, key):
        if key=="book":
            keys=['key',
            'author',
            'editor',
            'title',
            'publisher',
            'year',
            'volume',
            'series',
            'address',
            'edition',
            'month',
            'note']
            return keys
    
    

'''    author = input("Book's author: ")
        elif author_or_editor == '2':
            while editor == '':
                editor = input("Book's editor: ")
        while title == '':
            title = input("Book's title: ")
        while publisher == '':
            publisher = input("Book's publisher: ")
        while year == '':
            year = input("Publishing year: ")
        volume = input("Book's volume/number(optional): ")
        series = input("Book's series(optional): ")
        address = input("Book's address(optional): ")
        edition = input("Book's edition(optional): ")
        month = input("Publishing month(optional): ")
        note = input("Book's note(optional): ")'''