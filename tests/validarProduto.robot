*** Settings ***
Library    D:/projetos/CNAB/resources/cnab_keywords.py

*** Variables ***
${CAMINHO_ARQUIVO}        D:/projetos/CNAB/resources/BRFNT.RB40.CCE4.27092024.035556.RET
@{PRODUTOS_CONHECIDOS}    E    # Troque para R e teste

*** Test Cases ***
Validar Produto Conhecido no Arquivo CNAB 240
    [Documentation]    Este teste valida se os produtos no arquivo CNAB 240 são conhecidos.
    
    # Chama a função de validação de produtos
    ${resultado}    ${mensagem}=    Validar Produto    ${CAMINHO_ARQUIVO}    @{PRODUTOS_CONHECIDOS}

    # Verifica se a validação foi bem-sucedida
    Run Keyword If    ${resultado} == True    Log    ${mensagem}
    Run Keyword If    ${resultado} == False    Fail    ${mensagem}

