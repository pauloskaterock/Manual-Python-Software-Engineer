
# Projeto 1: Consultar uma API de Clima
# Este projeto consulta uma API de clima para obter a previsão do tempo para uma cidade específica.


# import requests

# def get_weather(city):
#     api_key = 'sua_chave_api'
#     base_url = 'http://api.openweathermap.org/data/2.5/weather'
#     params = {'q': city, 'appid': api_key, 'units': 'metric'}
    
#     response = requests.get(base_url, params=params)
    
#     if response.status_code == 200:
#         data = response.json()
#         print(f"Clima em {city}: {data['weather'][0]['description']}")
#         print(f"Temperatura: {data['main']['temp']}°C")
#     else:
#         print("Cidade não encontrada ou erro na requisição.")

# # Teste a função
# get_weather('São Paulo')



# Projeto 2: Web Scraping de Notícias
# Este projeto realiza o scraping de títulos de notícias de um site de notícias usando a combinação de requests e BeautifulSoup.


# import requests
# from bs4 import BeautifulSoup

# def scrape_news():
#     url = 'https://www.bbc.com/news'
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')
        
#         for i, headline in enumerate(headlines, 1):
#             print(f"{i}. {headline.text}")
#     else:
#         print("Erro ao acessar o site de notícias.")

# # Teste a função
# scrape_news()



# Projeto 3: Enviar Dados de Formulário
# Este projeto simula o envio de dados de um formulário para um servidor.


# import requests

# def submit_form():
#     url = 'https://httpbin.org/post'
#     form_data = {'name': 'John Doe', 'email': 'john@example.com'}
    
#     response = requests.post(url, data=form_data)
    
#     if response.status_code == 200:
#         print("Formulário enviado com sucesso.")
#         print(response.json())
#     else:
#         print("Erro ao enviar o formulário.")

# # Teste a função
# submit_form()