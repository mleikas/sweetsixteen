*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Book Reference
    Add One Book
    Output Should Contain  "Which reference type book/article/misc/phdthesis/incollection ?:"

*** Keywords ***
Add One Book
    Input Value  2
    Start Program
    

    
    #[2, "book", "1", "Tove Jansson", "Publisher", "Taikatalvi", "1957", "", "", "", "", "", "", "", "BOOK991"]