def validar_header_lote_cnab240(caminho_arquivo):
    """
    Função para validar o header de lote do arquivo CNAB 240.
    """
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            
            # Validar se há pelo menos duas linhas no arquivo
            if len(linhas) < 2:
                raise Exception("Arquivo CNAB não contém header de lote.")
            
            # Header de lote é geralmente a segunda linha (índice 1)
            header_lote = linhas[1][:240]  # Pega apenas os primeiros 240 caracteres

            # Definir os valores esperados para alguns campos do header de lote
            valores_esperados = {
                "codigo_banco": "237",        # Posições 1-3: Código do banco
                "lote_servico": "0001",       # Posições 4-7: Número do lote de serviço
                "tipo_registro": "1",         # Posição 8: Tipo de registro
                "tipo_operacao": "C",         # Posição 9: Tipo de operação (C=Crédito)
                "tipo_servico": "01",         # Posições 10-11: Tipo de serviço
                "layout_lote": "030"          # Posições 14-16: Versão do layout do lote
            }

            # Extração dos campos do header de lote
            campos = {
                "codigo_banco": header_lote[0:3],      # Posições 1-3 (Código do Banco)
                "lote_servico": header_lote[3:7],      # Posições 4-7 (Lote de Serviço)
                "tipo_registro": header_lote[7:8],     # Posição 8 (Tipo de Registro)
                "tipo_operacao": header_lote[8:9],     # Posição 9 (Tipo de Operação)
                "tipo_servico": header_lote[9:11],     # Posições 10-11 (Tipo de Serviço)
                "layout_lote": header_lote[13:16],     # Posições 14-16 (Layout do Lote)
            }

            # Validar os campos extraídos com os valores esperados
            erros = []
            for campo, valor_esperado in valores_esperados.items():
                if campos[campo] != valor_esperado:
                    erros.append(f"{campo} incorreto: esperado {valor_esperado}, encontrado {campos[campo]}")

            # Verificar se há erros
            if erros:
                return False, erros
            else:
                return True, "Header de lote validado com sucesso."

    except FileNotFoundError:
        return False, f"Arquivo {caminho_arquivo} não encontrado."
    except Exception as e:
        return False, str(e)


# cnab_keywords.py

def ler_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
            return conteudo  # Retorna o conteúdo lido
    except Exception as e:
        return f"Erro ao ler o arquivo: {str(e)}"  # Retorna uma mensagem de erro




def validar_header_lote(caminho_arquivo):
    nome_banco_esperado = "BRADESCO"  # Substitua pelo nome correto do banco que você espera
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            header = arquivo.readline().strip()  # Lê a primeira linha do arquivo e remove espaços

            # Verifica se o nome do banco está presente no header
            if nome_banco_esperado in header:
                return True, 'Header validado com sucesso.'
            else:
                return False, f'Nome do banco incorreto: esperado "{nome_banco_esperado}", encontrado "{header}".'
    except Exception as e:
        return False, f"Erro ao ler o arquivo: {str(e)}"
    


    # cnab_keywords.py

# cnab_keywords.py

def validar_produto(caminho_arquivo, produtos_conhecidos):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            produtos_invalidos = []

            for linha in linhas[2:]:  # Pula o header
                produto = linha[13:14].strip()  # Exemplo de extração do produto

                if produto not in produtos_conhecidos:
                    produtos_invalidos.append(produto)

            if produtos_invalidos:
                return False, f'Produtos desconhecidos encontrados: {", ".join(produtos_invalidos)}'
            return True, 'Todos os produtos são conhecidos.'
    except Exception as e:
        return False, f"Erro ao ler o arquivo: {str(e)}"





# cnab_keywords.py
# cnab_keywords.py

def validar_produto_desconhecido(caminho_arquivo, produtos_conhecidos):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            produtos_desconhecidos = []
            
            # Itera sobre as linhas do arquivo (pulando o header)
            for linha in linhas[2:]:  # Começa na linha 1, supondo que a linha 0 é o header
                # Aqui você precisa adaptar a extração do produto de acordo com a estrutura do arquivo
                produto = linha[13:14].strip()  # Supondo que o código do produto está nas posições 15 a 20

                if produto not in produtos_conhecidos:
                    produtos_desconhecidos.append(produto)

            if produtos_desconhecidos:
                # Gere um aviso ou erro aqui
                for produto in produtos_desconhecidos:
                    print(f'Aviso: Produto desconhecido encontrado: {produto}')
                return False, f'Produtos desconhecidos encontrados: {", ".join(produtos_desconhecidos)}'
                
            return True, 'Todos os produtos são conhecidos.'
    except Exception as e:
        return False, f"Erro ao ler o arquivo: {str(e)}"
