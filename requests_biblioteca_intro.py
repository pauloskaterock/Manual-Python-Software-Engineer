
# A biblioteca requests do Python é uma biblioteca popular usada para enviar requisições HTTP de forma simples e intuitiva. Ela permite que você interaja com APIs web, envie dados a um servidor e receba respostas com facilidade.

# Instalação
# Antes de usar a biblioteca requests, você precisa instalá-la. Você pode fazer isso usando o pip:


# pip install requests
# Uso Básico da Biblioteca requests
# 1. Enviar uma Requisição GET


# import requests

# response = requests.get('https://api.github.com')
# print(response.status_code)  # Exibe o código de status da resposta
# print(response.json())       # Exibe o conteúdo da resposta em formato JSON


# 2. Enviar uma Requisição POST


# import requests

# url = 'https://httpbin.org/post'
# data = {'key': 'value'}

# response = requests.post(url, data=data)
# print(response.status_code)  # Exibe o código de status da resposta
# print(response.json())       # Exibe o conteúdo da resposta em formato JSON


# 3. Enviar Dados JSON


# import requests

# url = 'https://httpbin.org/post'
# json_data = {'key': 'value'}

# response = requests.post(url, json=json_data)
# print(response.status_code)  # Exibe o código de status da resposta
# print(response.json())       # Exibe o conteúdo da resposta em formato JSON


# 4. Enviar Cabeçalhos Personalizados


# import requests

# url = 'https://api.github.com'
# headers = {'User-Agent': 'my-app'}

# response = requests.get(url, headers=headers)
# print(response.status_code)  # Exibe o código de status da resposta
# print(response.json())       # Exibe o conteúdo da resposta em formato JSON


# 5. Manipular Parâmetros da URL


# import requests

# url = 'https://httpbin.org/get'
# params = {'param1': 'value1', 'param2': 'value2'}

# response = requests.get(url, params=params)
# print(response.status_code)  # Exibe o código de status da resposta
# print(response.url)          # Exibe a URL completa com parâmetros
# print(response.json())       # Exibe o conteúdo da resposta em formato JSON


# A biblioteca requests simplifica a interação com a web e APIs, tornando o envio de requisições HTTP uma tarefa fácil. Aprender a usar requests com diferentes tipos de requisições, cabeçalhos personalizados, parâmetros de URL e manipulação de respostas é essencial para quem deseja trabalhar com web scraping, integração de APIs e desenvolvimento de aplicações web.