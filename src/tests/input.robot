*** Settings ***
Resource  resource.robot

*** Keywords ***
Add One Book
    Input Value  3  # add book
    Input Value  key 1
    Input Value  1
    Input Value  Tove Jansson
    Input Value  ""
    Input Value  Muumilaakson Marraskuu
    Input Value  WSOY
    Input Value  1970
    Input Value  ""
    Input Value  ""
    Input Value  ""
    Input Value  ""
    Input Value  ""
    Input Value  ""

*** Test Cases ***
Add Book Reference
    Start Program
    Add One Book
    Reference Count Should Be  1


