# # Projetos Práticos com NumPy
# # 1. Análise de Dados Básica

# import numpy as np

# # Dados fictícios de vendas
# vendas = np.array([100, 150, 200, 250, 300, 350, 400, 450, 500])

# # Estatísticas básicas
# print("Total de vendas:", np.sum(vendas))
# print("Média de vendas:", np.mean(vendas))
# print("Maior venda:", np.max(vendas))
# print("Menor venda:", np.min(vendas))

# #-------------------------------------------------------------------------------------------------------------
# # 2. Processamento de Imagens
# # NumPy é frequentemente usado para manipular imagens, que podem ser representadas como arrays de pixels.


# from PIL import Image
# import numpy as np

# # Carregar uma imagem e converter para array NumPy
# img = Image.open('path_to_image.jpg')
# img_array = np.array(img)

# # Converter a imagem para escala de cinza
# gray_img_array = np.mean(img_array, axis=2)

# # Converter o array de volta para uma imagem e salvar
# gray_img = Image.fromarray(gray_img_array.astype(np.uint8))
# gray_img.save('gray_image.jpg')


# # --------------------------------------------------------------------------------------------------

# # 3. Simulação de Dados
# # Você pode usar NumPy para gerar dados aleatórios para simulações.


# import numpy as np

# # Gerar 1000 amostras de uma distribuição normal
# data = np.random.randn(1000)

# # Calcular estatísticas
# mean = np.mean(data)
# std_dev = np.std(data)

# print("Média:", mean)
# print("Desvio Padrão:", std_dev)