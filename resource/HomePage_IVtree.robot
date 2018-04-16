*** Settings ***
Documentation    IVTree project for automation suite
...
Library          OperatingSystem
Library          ../lib/IVTreeHomePage.py

*** Variables ***
${Browser}        Chrome
${SiteUrl}        https://ivtree.com/
${email}          pappu.kumar@ivtree.com
${emailResponse}        Oops. Something went wrong. Please try again later
${Testcase ID}      Verify_IVtree_Page

*** Test Cases ***
Navigate to the Home Page:
    [Tags]    Ivtree navigation modules through home and Company
    Open Browser to the IVTree Page
    Navigation module for HomeCompany
#    Verify email response
    [Teardown]      Close Browser

Selecting Product:
    [Tags]      Ivtree Product modules for sale department
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser

Verify Product:
    [Tags]      Verify Product listed
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Verify Modules:
    [Tags]      Verify Product modules listed
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Verify Product Feature:
    [Tags]      Verify Product Freature
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser

Verify Features :
    [Tags]      Verify all festures
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser

Collecting Data:
    [Tags]      Collecting all inforation
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Validate Information:
    [Tags]      Validating information
    Open Browser to the IVTree Page
    Product module fo sales
    [Teardown]      Close Browser
Validate Data:
    [Tags]      Validate data
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Verify Product Info:
    [Tags]      Verify all product info
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Connecting to server
    [Tags]      Connecting to server 
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Validate connection
    [Tags]      Validate connection
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Verify server info
    [Tags]      Verify server info
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Connecting to client
    [Tags]      Connecting to client
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Validate connection of client
    [Tags]      Validate connection of client
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Verify client info
    [Tags]      Verify client info
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Getting request from client
    [Tags]      Getting request from client
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Getting response from server
    [Tags]      Getting response from server
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser
Accepting request from client
    [Tags]      Accepting request from client
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]      Close Browser

Closing connection
    [Tags]      Accepting request from client
    Open Browser to the IVTree Page
    Product module for sales
    [Teardown]
#TestCase--03:
#    [Tags]  Client area with sigunup form


*** Keywords ***
Open Browser to the IVTree Page
    [Documentation]  Open Mentioned Browser From Variable And Pass Respective Url from Variable To UrlField
    open browser      ${SiteUrl}    ${Browser}
    Maximize Browser Window
Navigation module for HomeCompany
    Navigate_Between_HomeCompany        ${email}


Verify email response
    location should contain  ${emailResponse}

Product module for sales
    Products_Module






#Welcome Page Should Be
#    [Documentation]  Verify DashBoardPage page
##    Location Should Be    ${WELCOME URL}
#    Title Should Be
