# # NumPy é uma biblioteca fundamental para a computação científica em Python. Ela fornece suporte para arrays multidimensionais e matrizes, além de uma ampla coleção de funções matemáticas para operar nesses arrays. NumPy é a base de muitas outras bibliotecas científicas e de machine learning, como Pandas, SciPy, Scikit-learn e TensorFlow.

# # Conceitos Básicos do NumPy
# # Instalação
# # Para instalar NumPy, você pode usar o pip:


# # pip install numpy
# # Importação
# #----------------------------------------------------------------------------
# # import numpy as np
# # Criação de Arrays
# # Arrays são a estrutura de dados central de NumPy. Aqui estão algumas maneiras de criar arrays:

# # Array a partir de uma lista:

# a = np.array([1, 2, 3])
# print(a)

# # Array multidimensional (matriz):


# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)

# # Funções de criação de arrays:


# zeros = np.zeros((2, 3))  # Array de zeros
# ones = np.ones((2, 3))    # Array de uns
# identity = np.eye(3)      # Matriz identidade

# # Operações Básicas com Arrays
# # Operações Matemáticas
# # NumPy permite realizar operações matemáticas em arrays de forma eficiente:


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# # Adição
# c = a + b
# print(c)

# # Subtração
# d = a - b
# print(d)

# # Multiplicação element-wise
# e = a * b
# print(e)

# # Divisão element-wise
# f = a / b
# print(f)

# # Funções Universais (ufuncs)
# # NumPy fornece muitas funções matemáticas que operam em arrays:


# a = np.array([1, 2, 3])
# print(np.sqrt(a))  # Raiz quadrada
# print(np.exp(a))   # Exponencial
# print(np.mean(a))  # Média
# print(np.std(a))   # Desvio padrão

# # Indexação e Fatiamento
# # Você pode acessar elementos específicos e fatias de arrays:

# a = np.array([1, 2, 3, 4, 5, 6])

# # Acessando elementos
# print(a[0])  # Primeiro elemento
# print(a[-1]) # Último elemento

# # Fatiamento
# print(a[1:4]) # Elementos do índice 1 ao 3
# print(a[:3])  # Primeiros três elementos
# print(a[3:])  # Elementos a partir do índice 3



# # NumPy é uma biblioteca poderosa que permite a manipulação eficiente de arrays e matrizes, além de fornecer uma ampla gama de funções matemáticas. Com suas capacidades, NumPy é uma ferramenta essencial para qualquer cientista de dados ou engenheiro que trabalhe com Python. Estudar e praticar com NumPy abrirá portas para projetos mais avançados em análise de dados, machine learning e ciência de dados.