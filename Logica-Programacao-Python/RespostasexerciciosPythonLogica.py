# # Programa que solicita dois números e exibe a soma:


# # num1 = float(input("Digite o primeiro número: "))
# # num2 = float(input("Digite o segundo número: "))
# # soma = num1 + num2
# # print("A soma é:", soma)
# ----------------------------------------------------------------
# # Programa que calcula a área de um círculo:

# # import math

# # raio = float(input("Digite o raio do círculo: "))
# # area = math.pi * raio ** 2
# # print("A área do círculo é:", area)
# -----------------------------------------------------------
# # Verificar se um número é par ou ímpar:

# # numero = int(input("Digite um número: "))
# # if numero % 2 == 0:
# #     print("O número é par.")
# # else:
# #     print("O número é ímpar.")
# -----------------------------------------------------------
# # Encontrar o maior de três números:

# # num1 = float(input("Digite o primeiro número: "))
# # num2 = float(input("Digite o segundo número: "))
# # num3 = float(input("Digite o terceiro número: "))
# # maior = max(num1, num2, num3)
# # print("O maior número é:", maior)
# --------------------------------------------------------
# # Calcular o fatorial de um número:

# # num = int(input("Digite um número: "))
# # fatorial = 1
# # for i in range(1, num + 1):
# #     fatorial *= i
# # print("O fatorial de", num, "é:", fatorial)
# --------------------------------------------------------
# # Encontrar o maior e o menor de uma lista de números:

# # numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]
# # maior = max(numeros)
# # menor = min(numeros)
# # print("O maior número é:", maior)
# # print("O menor número é:", menor)
# ------------------------------------------------------
# # Verificar se um número é primo:

# # def eh_primo(num):
# #     if num <= 1:
# #         return False
# #     for i in range(2, int(num ** 0.5) + 1):
# #         if num % i == 0:
# #             return False
# #     return True

# # numero = int(input("Digite um número: "))
# # if eh_primo(numero):
# #     print("O número é primo.")
# # else:
# # #     print("O número não é primo.")
# ---------------------------------------------------------
# # # Exibir apenas os números pares de uma lista:

# # numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]
# # pares = [num for num in numeros if num % 2 == 0]
# # print("Os números pares são:", pares)
# ---------------------------------------------------------
# # # Converter graus Celsius para Fahrenheit:

# # celsius = float(input("Digite a temperatura em graus Celsius: "))
# # fahrenheit = (celsius * 9/5) + 32
# # print("A temperatura em Fahrenheit é:", fahrenheit)
# ---------------------------------------------------------
# # # Exibir apenas os números ímpares de uma lista:

# # numeros = [int(x) for x in input("Digite uma lista de números separados por espaço: ").split()]
# # impares = [num for num in numeros if num % 2 != 0]
# # print("Os números ímpares são:", impares)