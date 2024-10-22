*** Settings ***
Library    D:/projetos/CNAB/resources/cnab_keywords.py

*** Variables ***
${CAMINHO_ARQUIVO}    D:/projetos/CNAB/resources/BRFNT.RB40.CCE4.27092024.035556.RET
@{PRODUTOS_CONHECIDOS}  E  # Liste os produtos conhecidos

*** Test Cases ***
Validar Produtos Desconhecidos no Arquivo CNAB 240
    [Documentation]    Este teste verifica se há produtos desconhecidos no arquivo CNAB 240.
    
    # Chama a função de validação de produtos desconhecidos
    ${resultado}    ${mensagem}=    Validar Produto Desconhecido    ${CAMINHO_ARQUIVO}    @{PRODUTOS_CONHECIDOS}

    # Verifica se a validação foi bem-sucedida
    Run Keyword If    ${resultado} == True    Log    ${mensagem} Não há produtos desconhencidos
    Run Keyword If    ${resultado} == False    Fail    ${mensagem} Produto desconhencido na coluna 14
