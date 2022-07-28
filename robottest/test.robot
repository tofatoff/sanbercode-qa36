***Settings***
Library     SeleniumLibrary


***Variables***
${url}  https://opensource-demo.orangehrmlive.com
${usernameFill}  id=txtUsername
${passwordFill}  id=txtPassword


***Test Cases***
Open Browser
    Open Browser    https://opensource-demo.orangehrmlive.com   chrome
    Input Text      ${username}     username
    Input Text      ${password}     password