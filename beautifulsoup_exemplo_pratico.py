# Exemplo Básico
# Aqui está um exemplo básico de uso do BeautifulSoup para extrair títulos de artigos de um site de notícias fictício.


# import requests
# from bs4 import BeautifulSoup

# URL do site
# url = 'http://exemplo.com/noticias'

# Fazendo a requisição
# response = requests.get(url)

# # Parseando o HTML
# soup = BeautifulSoup(response.text, 'html.parser')

# # Extraindo títulos de artigos
# titulos = soup.find_all('h2', class_='titulo-artigo')

# for titulo in titulos:
#     print(titulo.text)