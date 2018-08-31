*** Settings ***
Library    SeleniumLibrary
Library    CustomLibrary

*** Test Cases ***
Re-open browser 100 times
    :FOR    ${i}    IN RANGE    10
    \    Go to chrome and search something
    \    Async Close Browser
    # \    Close browser

*** Variables ***
${searchInput}=    id=lst-ib

*** Keywords ***
Go to chrome and search something
    Open Browser    https://www.google.com/    Chrome
    Search    selenium
    Wait Until Page Contains Element    xpath://*[text()='https://www.seleniumhq.org/']

Search
    [Arguments]    ${text}
    Wait Until Page Contains Element    ${searchInput}    timeout=5s
    Wait Until Element Is Visible    ${searchInput}    timeout=1s
    Input Text    ${searchInput}    ${text}
    Press Key    ${searchInput}    \\13
