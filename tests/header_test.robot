*** Settings ***
Library    D:/projetos/CNAB/resources/cnab_keywords.py  # Certifique-se de que o caminho está correto

*** Variables ***
${CAMINHO_ARQUIVO}    D:/projetos/CNAB/resources/BRFNT.RB40.CCE4.27092024.035556.RET  # Caminho para o arquivo

*** Test Cases ***
Validar Header de Lote do Arquivo CNAB 240
    [Documentation]    Este teste valida o nome do banco no header de lote do arquivo CNAB 240.
    
    # Chama a função de validação do header
    ${resultado}    ${mensagem}=    Validar Header Lote    ${CAMINHO_ARQUIVO}

    # Verifica se a validação foi bem-sucedida
    Run Keyword If    ${resultado} == True    Log    ${mensagem}
    Run Keyword If    ${resultado} == False    Fail    ${mensagem}
