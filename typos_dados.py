# Em Python, existem vários tipos de dados embutidos que permitem armazenar diferentes tipos de valores. Aqui estão os tipos de dados mais comuns:

# Tipos de Dados Simples
# Inteiros (int)

# Representam números inteiros, positivos ou negativos, sem parte decimal.

# x = 10
# y = -5
# Ponto Flutuante (float)

# Representam números reais, contendo parte inteira e parte decimal.

# x = 10.5
# y = -5.75
# Complexos (complex)

# Representam números complexos com parte real e imaginária.

# x = 1 + 2j
# y = complex(3, -4)
# Booleanos (bool)

# Representam valores de Verdadeiro ou Falso.

# x = True
# y = False
# Strings (str)

# Representam cadeias de caracteres (texto).

# x = "Hello"
# y = 'World'
# Tipos de Dados Compostos
# Listas (list)

# Coleções ordenadas de elementos que podem ser de tipos diferentes.

# x = [1, 2, 3, "apple", 4.5]
# Tuplas (tuple)

# Coleções ordenadas e imutáveis de elementos.

# x = (1, 2, 3, "banana", 4.5)
# Conjuntos (set)

# Coleções não ordenadas de elementos únicos.

# x = {1, 2, 3, "cherry", 4.5}
# Dicionários (dict)

# Coleções de pares chave-valor.

# x = {"name": "John", "age": 30, "city": "New York"}
# Exemplos Práticos
# Inteiros e Ponto Flutuante

# a = 10       # int
# b = 3.14     # float

# print(type(a))  # <class 'int'>
# print(type(b))  # <class 'float'>
# Complexos

# c = 1 + 2j  # complex
# d = complex(3, -4)

# print(type(c))  # <class 'complex'>
# print(d.real)   # 3.0
# print(d.imag)   # -4.0
# Booleanos

# is_sunny = True  # bool
# is_raining = False

# print(type(is_sunny))  # <class 'bool'>
# Strings

# greeting = "Hello, World!"  # str

# print(type(greeting))  # <class 'str'>
# print(greeting[0])     # H
# print(greeting[7:12])  # World
# Listas

# fruits = ["apple", "banana", "cherry"]
# numbers = [1, 2, 3, 4, 5]

# print(type(fruits))    # <class 'list'>
# print(fruits[1])       # banana
# print(numbers[-1])     # 5
# Tuplas

# point = (10, 20)
# person = ("Alice", 30)

# print(type(point))     # <class 'tuple'>
# print(person[0])       # Alice
# Conjuntos

# unique_numbers = {1, 2, 3, 4, 4, 5}

# print(type(unique_numbers))  # <class 'set'>
# print(unique_numbers)        # {1, 2, 3, 4, 5}
# Dicionários

# student = {"name": "John", "age": 21, "courses": ["Math", "Science"]}

# print(type(student))         # <class 'dict'>
# print(student["name"])       # John
# print(student["courses"][0]) # Math
# Conversão de Tipos

# Python permite converter entre diferentes tipos de dados, utilizando funções de 
# conversão de tipo, como int(), float(), str(), list(), tuple(), set(), e dict().

# Exemplo de Conversão de Tipos

# # Convertendo de int para float
# num = 10
# num_float = float(num)
# print(type(num_float))  # <class 'float'>

# # Convertendo de float para int
# pi = 3.14
# pi_int = int(pi)
# print(type(pi_int))  # <class 'int'>

# # Convertendo de list para set
# fruits_list = ["apple", "banana", "cherry"]
# fruits_set = set(fruits_list)
# print(type(fruits_set))  # <class 'set'>


# Com esses exemplos e explicações, você deve ter uma boa compreensão dos diferentes tipos de dados em Python e como utilizá-los.





