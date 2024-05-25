# Em Python, operadores de comparação são usados para comparar valores. Eles retornam um valor booleano (True ou False). Abaixo estão os operadores de comparação mais comuns, acompanhados de exemplos de código:

# Igualdade (==): Verifica se dois valores são iguais.


a = 5
b = 5
c = 10
print(a == b)  # True
print(a == c)  # False

# Diferença (!=): Verifica se dois valores são diferentes.


a = 5
b = 5
c = 10
print(a != b)  # False
print(a != c)  # True

# Maior que (>): Verifica se o valor à esquerda é maior que o valor à direita.

a = 5
b = 3
c = 7
print(a > b)  # True
print(a > c)  # False

# Menor que (<): Verifica se o valor à esquerda é menor que o valor à direita.


a = 5
b = 3
c = 7
print(a < b)  # False
print(a < c)  # True

# Maior ou igual a (>=): Verifica se o valor à esquerda é maior ou igual ao valor à direita.


a = 5
b = 5
c = 3
print(a >= b)  # True
print(a >= c)  # True

# Menor ou igual a (<=): Verifica se o valor à esquerda é menor ou igual ao valor à direita.


a = 5
b = 5
c = 7
print(a <= b)  # True
print(a <= c)  # True

# Exemplos com diferentes tipos de dados
# Os operadores de comparação podem ser usados com diferentes tipos de dados, incluindo inteiros, floats, strings, listas, e muito mais. Aqui estão alguns exemplos adicionais:

# Comparação de Strings

str1 = "apple"
str2 = "banana"
print(str1 == str2)  # False
print(str1 != str2)  # True
print(str1 < str2)   # True, porque "apple" vem antes de "banana" em ordem alfabética
print(str1 > str2)   # False

# Comparação de Listas

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
print(list1 == list2)  # True
print(list1 != list3)  # True
print(list1 < list3)   # True, comparação lexicográfica
print(list1 > list3)   # False

# Comparação de Números de Ponto Flutuante

x = 10.5
y = 20.7
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False

# Uso em Estruturas de Controle
# Os operadores de comparação são frequentemente usados em estruturas de controle, como instruções if, loops while, e compreensão de listas.


# # Estrutura de controle if
a = 10
b = 20
if a < b:
    print("a é menor que b")

# Loop while
count = 0
while count < 5:
    print(count)
    count += 1

# Compreensão de listas
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers if x > 2]
print(squares)  # [9, 16, 25]

# Esses exemplos mostram como os operadores de comparação podem ser usados de maneira versátil em Python para comparar valores e tomar decisões baseadas nessas comparações.