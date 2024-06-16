Este repositório contém um script em Python para converter arquivos XML em um formato de planilha Excel. O script lê arquivos XML de um diretório específico, extrai dados específicos e armazena essas informações em um arquivo Excel. Esta versão do script adiciona uma linha para cada chave NFe encontrada.

** Requisitos **:
- Python 
- Bibliotecas Python:
- os
- xmltodict
- pandas
- openpyxl


** Funcionalidades **:
- Lê arquivos XML de um diretório específico.
- Extrai dados específicos dos arquivos XML.
- Armazena os dados extraídos em um DataFrame do Pandas.
- Exporta os dados do DataFrame para um arquivo Excel.

** Como usar **:
- Coloque seus arquivos XML no diretório cte.
- Execute o script.
- O script irá gerar um arquivo Excel chamado CTes_linhas.xlsx no mesmo diretório do script, contendo as chaves extraídas dos arquivos XML.

** Observações **:
- Certifique-se de que os arquivos XML estejam no formato esperado pelo script.
- O script espera que a estrutura XML contenha as seções cteProc e subsequentes conforme descrito no código.

** Diferenças em relação ao script com display em colunas **
- Estrutura da Tabela: Esta versão cria uma linha para cada chave NFe encontrada, enquanto a versão anterior cria colunas separadas para as chaves NFe1 e NFe2.
- Colunas do DataFrame: Esta versão define as colunas do DataFrame como ['Chave CTe', 'Chave NFe'], enquanto a versão anterior define como ['Chave CTe', 'Chave NFe1', 'Chave NFe2'].
- Manuseio de Chaves NFe: Esta versão adiciona uma linha separada para cada chave NFe encontrada, possibilitando um número variável de chaves NFe por CTe. Na versão anterior, até duas chaves NFe são armazenadas em colunas fixas.
