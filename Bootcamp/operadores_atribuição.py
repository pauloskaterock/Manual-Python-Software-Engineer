# Os operadores de atribuição em Python são usados para atribuir valores a variáveis. Atribuição simples, composta e operações com operadores aritméticos são exemplos comuns de como os operadores de atribuição são usados em Python.

# Aqui estão os principais operadores de atribuição com exemplos:

# 1. Atribuição Simples (=)
# Atribui um valor a uma variável.


x = 10
print(x)  # Saída: 10


# 2. Atribuição de Adição (+=)
# Adiciona um valor à variável e atribui o resultado à variável.


x = 5
x += 3  # Equivalente a x = x + 3
print(x)  # Saída: 8

# 3. Atribuição de Subtração (-=)
# Subtrai um valor da variável e atribui o resultado à variável.


x = 5
x -= 2  # Equivalente a x = x - 2
print(x)  # Saída: 3

# 4. Atribuição de Multiplicação (*=)
# Multiplica a variável por um valor e atribui o resultado à variável.

x = 5
x *= 2  # Equivalente a x = x * 2
print(x)  # Saída: 10

# 5. Atribuição de Divisão (/=)
# Divide a variável por um valor e atribui o resultado à variável.


x = 10
x /= 2  # Equivalente a x = x / 2
print(x)  # Saída: 5.0

# 6. Atribuição de Módulo (%=)
# Calcula o módulo da variável e atribui o resultado à variável.


x = 10
x %= 3  # Equivalente a x = x % 3
print(x)  # Saída: 1

# 7. Atribuição de Divisão Inteira (//=)
# Realiza a divisão inteira da variável por um valor e atribui o resultado à variável.


x = 10
x //= 3  # Equivalente a x = x // 3
print(x)  # Saída: 3

# 8. Atribuição de Exponenciação (**=)
# Eleva a variável à potência de um valor e atribui o resultado à variável.


x = 2
x **= 3  # Equivalente a x = x ** 3
print(x)  # Saída: 8

# 9. Atribuição de Bitwise AND (&=)
# Aplica o operador bitwise AND e atribui o resultado à variável.


x = 5  # 101 em binário
x &= 3  # 011 em binário; Equivalente a x = x & 3
print(x)  # Saída: 1 (001 em binário)

# 10. Atribuição de Bitwise OR (|=)
# Aplica o operador bitwise OR e atribui o resultado à variável.


x = 5  # 101 em binário
x |= 3  # 011 em binário; Equivalente a x = x | 3
print(x)  # Saída: 7 (111 em binário)

# 11. Atribuição de Bitwise XOR (^=)
# Aplica o operador bitwise XOR e atribui o resultado à variável.


x = 5  # 101 em binário
x ^= 3  # 011 em binário; Equivalente a x = x ^ 3
print(x)  # Saída: 6 (110 em binário)

# 12. Atribuição de Shift à Esquerda (<<=)
# Desloca os bits da variável para a esquerda e atribui o resultado à variável.


x = 5  # 101 em binário
x <<= 1  # Equivalente a x = x << 1
print(x)  # Saída: 10 (1010 em binário)

# 13. Atribuição de Shift à Direita (>>=)
# Desloca os bits da variável para a direita e atribui o resultado à variável.

x = 5  # 101 em binário
x >>= 1  # Equivalente a x = x >> 1
print(x)  # Saída: 2 (10 em binário)

# Esses operadores ajudam a simplificar e otimizar o código, evitando a necessidade de reescrever a variável na operação de atribuição.