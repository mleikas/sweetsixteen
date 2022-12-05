*** Settings ***
Resource  resource.robot

*** Test Cases ***
Add Book Reference
    Add One Book
    Reference Count Should Be  1

*** Keywords ***
Add One Book
    Input Value  2  # add reference
    Input Value  book
    Input Value  key
    Input Value  1
    Input Value  ""
    Input Value  Tove Jansson
    Input Value  ""
    Input Value  ""
    Input Value  ""
    Input Value  ""
    Input Value  WSOY
    Input Value  ""
    Input Value  Taikatalvi
    Input Value  ""
    Input Value  1957
    Input Value  Tove
    Input Value  Jansson
    Input Value  ""