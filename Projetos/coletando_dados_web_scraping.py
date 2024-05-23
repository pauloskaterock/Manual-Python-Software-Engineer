from bs4 import BeautifulSoup
import requests

# Site que será coletado
site = "http://www.pudim.com.br/"

# Coleta os dados do site
html = requests.get(site).content

# Formatando os dados
dados = BeautifulSoup(html, 'html.parser')

# coletando a classe "emailme" que contém o e-mail
email = dados.find("div", class_="emailme")

if email:
    # coletando a tag dentro da div email
    link = email.find("a")
    
    # coletando apenas o texto
    print("1", link)  
    print("2", link.text)
    
    # coletando o endereço do link
    print("3", link['href'])
else:
    print("Não foi possível encontrar o e-mail.")
