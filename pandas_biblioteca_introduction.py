# # A biblioteca Pandas é uma das ferramentas mais poderosas e versáteis para manipulação e análise de dados em Python. Ela oferece estruturas de dados e funções que facilitam o trabalho com grandes conjuntos de dados, permitindo operações como leitura, limpeza, transformação e visualização de dados de maneira eficiente.

# # Introdução ao Pandas
# # Pandas fornece duas principais estruturas de dados:

# # Series: Um array unidimensional, semelhante a uma coluna em uma tabela.
# # DataFrame: Uma estrutura de dados bidimensional, semelhante a uma tabela com linhas e colunas.
# # Instalação
# # Para instalar a biblioteca Pandas, você pode usar o pip:


# # pip install pandas
# # Importação
# #------------------------------------------------------------------------------------------------
# import pandas as pd
# # Exemplos Básicos
# # Criar uma Series
# #------------------------------------------------------------------------------------------------
# import pandas as pd

# # Criar uma Series a partir de uma lista
# s = pd.Series([1, 3, 5, 7, 9])
# print(s)
# # Criar um DataFrame
# #------------------------------------------------------------------------------------------------
# import pandas as pd

# # Criar um DataFrame a partir de um dicionário
# data = {
#     'Nome': ['Alice', 'Bob', 'Charlie'],
#     'Idade': [25, 30, 35],
#     'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
# }
# df = pd.DataFrame(data)
# print(df)
# # Operações Básicas com DataFrame
# # Leitura de Dados
# # Pandas permite ler dados de diversos formatos, como CSV, Excel, SQL, JSON, etc.

# #------------------------------------------------------------------------------------------------
# # Ler dados de um arquivo CSV
# df = pd.read_csv('caminho/para/arquivo.csv')

# # Ler dados de um arquivo Excel
# df = pd.read_excel('caminho/para/arquivo.xlsx')
# # Acesso a Dados
# #------------------------------------------------------------------------------------------------
# # Selecionar uma coluna
# print(df['Nome'])

# # Selecionar múltiplas colunas
# print(df[['Nome', 'Idade']])

# # Selecionar uma linha pelo índice
# print(df.loc[0])

# # Selecionar um intervalo de linhas
# print(df[0:2])
# # Filtragem de Dados
# #------------------------------------------------------------------------------------------------
# # Filtrar dados baseados em uma condição
# print(df[df['Idade'] > 30])
# # Manipulação de Dados
# #------------------------------------------------------------------------------------------------
# # Adicionar uma nova coluna
# df['Salário'] = [50000, 60000, 70000]

# # Modificar valores
# df.loc[1, 'Idade'] = 31

# # Remover uma coluna
# df.drop('Salário', axis=1, inplace=True)


# # Projetos Práticos

# # Projeto 1: Análise de Dados de Vendas
# # Objetivo: Analisar um conjunto de dados de vendas para extrair insights sobre as vendas mensais, produtos mais vendidos, e o desempenho das lojas.

# # Leitura dos Dados:
# #------------------------------------------------------------------------------------------------
# df = pd.read_csv('vendas.csv')
# # Limpeza dos Dados:
# #------------------------------------------------------------------------------------------------
# # Remover linhas com valores nulos
# df.dropna(inplace=True)

# # Converter colunas para tipos apropriados
# df['Data'] = pd.to_datetime(df['Data'])
# df['Quantidade'] = df['Quantidade'].astype(int)
# # Análise Exploratória:
# #------------------------------------------------------------------------------------------------
# # Vendas totais por mês
# vendas_mensais = df.groupby(df['Data'].dt.month)['Valor'].sum()
# print(vendas_mensais)

# # Produto mais vendido
# produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()
# print(f"Produto mais vendido: {produto_mais_vendido}")

# # Desempenho das lojas
# desempenho_lojas = df.groupby('Loja')['Valor'].sum()
# print(desempenho_lojas)
# # Visualização de Dados:
# #------------------------------------------------------------------------------------------------
# import matplotlib.pyplot as plt

# # Gráfico de vendas mensais
# vendas_mensais.plot(kind='bar')
# plt.title('Vendas Mensais')
# plt.xlabel('Mês')
# plt.ylabel('Valor')
# plt.show()

# # Projeto 2: Análise de Dados de Redes Sociais
# # Objetivo: Analisar um conjunto de dados de redes sociais para entender o engajamento dos usuários, os horários de pico de atividade e identificar tendências.

# # Leitura dos Dados:
# #------------------------------------------------------------------------------------------------
# df = pd.read_json('redes_sociais.json')
# # Limpeza dos Dados:
# #------------------------------------------------------------------------------------------------
# # Remover duplicatas
# df.drop_duplicates(inplace=True)

# # Converter colunas para tipos apropriados
# df['Data_Hora'] = pd.to_datetime(df['Data_Hora'])
# # Análise Exploratória:
# #------------------------------------------------------------------------------------------------
# # Engajamento médio por post
# engajamento_medio = df['Engajamento'].mean()
# print(f"Engajamento médio: {engajamento_medio}")

# # Horários de pico de atividade
# horarios_pico = df['Data_Hora'].dt.hour.value_counts().sort_index()
# print(horarios_pico)

# # Tendências de hashtags
# hashtags_trend = df['Hashtags'].explode().value_counts()
# print(hashtags_trend)
# # Visualização de Dados:
# #------------------------------------------------------------------------------------------------
# # Gráfico de horários de pico de atividade
# horarios_pico.plot(kind='line')
# plt.title('Horários de Pico de Atividade')
# plt.xlabel('Hora do Dia')
# plt.ylabel('Número de Posts')
# plt.show()

# # Gráfico de tendências de hashtags
# hashtags_trend.head(10).plot(kind='bar')
# plt.title('Top 10 Hashtags')
# plt.xlabel('Hashtags')
# plt.ylabel('Frequência')
# plt.show()


# # Conclusão
# # Pandas é uma biblioteca essencial para quem trabalha com análise de dados em Python. Ela facilita a manipulação, análise e visualização de dados, sendo uma ferramenta poderosa para diversos tipos de projetos. Com a prática e o aprofundamento no uso de Pandas, você será capaz de realizar análises complexas de forma eficiente e eficaz.