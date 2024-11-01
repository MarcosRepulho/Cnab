*** Settings ***
Library    D:/projetos/CNAB/resources/cnab_keywords.py

*** Variables ***
${CAMINHO_ARQUIVO}    D:/projetos/CNAB/resources/BRFNT.RB40.CCE4.27092024.035556.RET

*** Test Cases ***
Validar Sentido do Arquivo CNAB 240
    [Documentation]    Este teste verifica se o sentido do arquivo CNAB é Retorno ou Remessa.
    ${resultado}    ${mensagem}=    Validar Sentido CNAB    ${CAMINHO_ARQUIVO}
    Run Keyword If    ${resultado} == True    Log    ${mensagem}
    Run Keyword If    ${resultado} == False    Fail    ${mensagem}
