*** Settings ***
Library    SeleniumLibrary
Library    CustomLibrary

*** Test Cases ***
Re-open browser 500 times
    :FOR    ${i}    IN RANGE    ${times}
    \    Go to chrome and search something
    \    Log To Console    ${i}
    # \    Async Close Browser
    \    Close browser

*** Variables ***
${headless} =    ${TRUE}
${title} =    xpath://h2[text()='What is Selenium?']
${times} =    100
# ${webDriverPath} =    ${CURDIR}/chromedriver/2.37/chromedriver.exe
${webDriverPath} =    ${CURDIR}/chromedriver/2.41/chromedriver.exe

*** Keywords ***
Go to chrome and search something
    Open Browser (in Headless)    https://www.seleniumhq.org/    Chrome
    Wait Page Contains "What is Selenium?"

Open Browser (in Headless)
    [Arguments]    ${url}    ${browser}
    ${options} =    Set Headless Options
    ${options} =    Change Log Level    options=${options}
    ${capabilities}=    Accept Insecure Certs
    Run Keyword If    ${headless}    Run Keywords
    ...               Create Webdriver    ${browser}    alias=ctmDriver    chrome_options=${options}    desired_capabilities=${capabilities}    executable_path=${webDriverPath}
    ...               AND    Go To    ${url}
    ...               ELSE    Open Browser    ${url}    ${browser}

Wait Page Contains "What is Selenium?"
    Wait Until Page Contains Element    ${title}    timeout=10s
    Wait Until Element Is Visible    ${title}    timeout=2s
