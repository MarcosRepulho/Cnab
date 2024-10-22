*** Settings ***
Library    D:/projetos/CNAB/resources/cnab_keywords.py  # Certifique-se de que o caminho está correto

*** Variables ***
${CAMINHO_ARQUIVO}    D:/projetos/CNAB/resources/BRFNT.RB40.CCE4.27092024.035556.RET  # Caminho para o arquivo

*** Test Cases ***
Ler Arquivo CNAB
    [Documentation]    Este teste lê o conteúdo do arquivo CNAB e exibe no log.
    
    # Chama a função para ler o arquivo
    ${conteudo} =    Ler Arquivo    ${CAMINHO_ARQUIVO}
    
    # Exibe o conteúdo lido no log
    Log    ${conteudo}
