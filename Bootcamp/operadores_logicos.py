# Em Python, os operadores lógicos são utilizados para combinar expressões condicionais e realizar operações booleanas. Aqui estão os operadores lógicos básicos, juntamente com exemplos de código para cada um:

# Operador and
# O operador and retorna True se ambas as expressões forem verdadeiras.


# # Exemplo 1
a = True
b = True
print(a and b)  # True

# # Exemplo 2
a = True
b = False
print(a and b)  # False

# # Exemplo 3
x = 5
y = 10
print(x > 0 and y > 0)  # True, pois ambas as condições são verdadeiras

# -----------------------------------------------------------------------------

# Operador or
# O operador or retorna True se pelo menos uma das expressões for verdadeira.


# # Exemplo 1
a = True
b = False
print(a or b)  # True

# # Exemplo 2
a = False
b = False
print(a or b)  # False

# # Exemplo 3
x = -5
y = 10
print(x > 0 or y > 0)  # True, pois uma das condições é verdadeira

# -----------------------------------------------------------------------------

# Operador not
# O operador not inverte o valor booleano da expressão.

# # Exemplo 1
a = True
print(not a)  # False

# # Exemplo 2
b = False
print(not b)  # True

# # Exemplo 3
x = 5
print(not x > 0)  # False, pois x > 0 é True, e not True é False

# -----------------------------------------------------------------------------

# Operador == (Igualdade)
# Verifica se duas expressões são iguais.


# # Exemplo 1
a = 5
b = 5
print(a == b)  # True

# # Exemplo 2
x = "hello"
y = "world"
print(x == y)  # False

# -----------------------------------------------------------------------------

# Operador != (Desigualdade)
# Verifica se duas expressões são diferentes.

# # Exemplo 1
a = 5
b = 10
print(a != b)  # True

# # Exemplo 2
x = "hello"
y = "hello"
print(x != y)  # False

# -----------------------------------------------------------------------------


# Operador > (Maior que)
# Verifica se a expressão à esquerda é maior que a expressão à direita.


# # Exemplo 1
a = 10
b = 5
print(a > b)  # True

# # Exemplo 2
x = 5
y = 10
print(x > y)  # False

# -----------------------------------------------------------------------------

# Operador < (Menor que)
# Verifica se a expressão à esquerda é menor que a expressão à direita.


# # Exemplo 1
a = 5
b = 10
print(a < b)  # True

# # Exemplo 2
x = 10
y = 5
print(x < y)  # False

# -----------------------------------------------------------------------------

# Operador >= (Maior ou igual a)
# Verifica se a expressão à esquerda é maior ou igual à expressão à direita.


# # Exemplo 1
a = 10
b = 5
print(a >= b)  # True

# # Exemplo 2
x = 5
y = 5
print(x >= y)  # True

# -----------------------------------------------------------------------------

# Operador <= (Menor ou igual a)
# Verifica se a expressão à esquerda é menor ou igual à expressão à direita.


# # Exemplo 1
a = 5
b = 10
print(a <= b)  # True

# # Exemplo 2
x = 5
y = 5
print(x <= y)  # True

# -----------------------------------------------------------------------------

# Combinação de Operadores Lógicos
# Você pode combinar vários operadores lógicos em uma única expressão:

# -----------------------------------------------------------------------------

x = 5
y = 10
z = 15

# Exemplo 1
print(x < y and y < z)  # True

# # Exemplo 2
print(x < y or y > z)  # True

# # Exemplo 3
print(not (x > y))  # True


# Esses exemplos cobrem os operadores lógicos básicos em Python, juntamente com exemplos de como eles são utilizados.