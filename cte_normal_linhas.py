import os
import xmltodict
import pandas as pd
import openpyxl

# Função para ler informações de um arquivo XML e extrair dados específicos
def ler_informacoes(nome_arquivo, valores):
    print(f'Processando arquivo: {nome_arquivo}')
    try:
        # Abre o arquivo XML para leitura
        with open(f'cte/{nome_arquivo}', 'rb') as arquivo_xml:
            # Converte o conteúdo XML para um dicionário Python
            dicionario_arquivo = xmltodict.parse(arquivo_xml)

            # Acessa a seção específica do XML (Personalizável)
            if "cteProc" in dicionario_arquivo:
                infos_nf = dicionario_arquivo["cteProc"]
                id_cte = infos_nf["CTe"]["infCte"]["@Id"]

                # Verifica se existe a seção infNFe e se é uma lista
                inf_nfe = infos_nf["CTe"]["infCte"]["infCTeNorm"]["infDoc"].get("infNFe", [])

                # Verifica o tipo de inf_nfe para evitar erros
                if not isinstance(inf_nfe, list):
                    inf_nfe = [inf_nfe]

                # Adiciona uma linha para cada chave NFe encontrada
                if inf_nfe:
                    for nfe in inf_nfe:
                        chave_nfe = nfe.get("chave")
                        if chave_nfe:
                            valores.append([id_cte, chave_nfe])
                else:
                    # Adiciona uma linha mesmo que não haja chaves NFe
                    valores.append([id_cte, None])

            else:
                print(f'Seção "cteProc" não encontrada no arquivo: {nome_arquivo}')

    except Exception as e:
        # Tratamento de erro caso ocorra algum problema ao processar o arquivo
        print(f'Erro ao processar {nome_arquivo}: {e}')

# Lista todos os arquivos no diretório 'cte'
lista_arquivos = os.listdir('cte')

# Define as colunas para o DataFrame
colunas = ['Chave CTe', 'Chave NFe']
valores = []

# Itera sobre cada arquivo na lista de arquivos
for arquivo in lista_arquivos:
    ler_informacoes(arquivo, valores)  # Chama a função para ler e extrair informações do arquivo

# Cria uma tabela com os dados extraídos
tabela = pd.DataFrame(columns=colunas, data=valores)

# Verifique se a tabela contém dados
print(tabela)

# Salva a tabela em uma planilha Excel
tabela.to_excel('CTes_linhas.xlsx', index=False)
