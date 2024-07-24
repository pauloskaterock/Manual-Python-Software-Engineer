# import requests
# from bs4 import BeautifulSoup

# # 1. Definir a URL da página a ser analisada
# url = 'https://example.com'

# # 2. Fazer uma requisição HTTP GET para a URL
# response = requests.get(url)

# # 3. Verificar se a requisição foi bem-sucedida
# if response.status_code == 200:
#     print("Conexão bem-sucedida!")
# else:
#     print(f"Erro na requisição: {response.status_code}")
#     exit()

# # 4. Parsear o conteúdo HTML da página com BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # 5. Extrair todos os links da página
# links = soup.find_all('a')

# print("\nLinks encontrados na página:")
# for link in links:
#     href = link.get('href')
#     texto = link.text.strip()
#     print(f"Texto: {texto}, URL: {href}")

# # 6. Se desejar, você pode extrair outras informações, como títulos da página
# titulo = soup.title.string
# print(f"\nTítulo da página: {titulo}")

# # 7. Exemplo adicional: Extrair todos os parágrafos de texto
# paragrafos = soup.find_all('p')

# print("\nParágrafos encontrados na página:")
# for p in paragrafos:
#     print(p.get_text())
