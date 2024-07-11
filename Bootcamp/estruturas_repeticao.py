# Em Python, as estruturas de repetição (ou laços) são usadas para executar um bloco de código múltiplas vezes. As duas principais estruturas de repetição são o for e o while. Vamos ver como cada uma funciona com exemplos práticos:

# Laço for:
# O laço for é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string).

# Exemplo 1: Iterar sobre uma lista


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Saída:
# apple
# banana
# cherry


# Exemplo 2: Usar range para iterar um número específico de vezes


for i in range(5):
    print(i)

# Saída:
# 0
# 1
# 2
# 3
# 4

# Exemplo 3: Iterar sobre as chaves de um dicionário


ages = {"Alice": 25, "Bob": 30, "Charlie": 35}
for name in ages:
    print(name, ages[name])

# Saída:
# Alice 25
# Bob 30
# Charlie 35


# Laço while:
# O laço while repete um bloco de código enquanto uma condição especificada é verdadeira. Ele é mais flexível que o for, mas deve-se tomar cuidado para evitar loops infinitos.

# Exemplo 1: Usar while para repetir um bloco até que uma condição seja falsa


count = 0
while count < 5:
    print(count)
    count += 1

# Saída:
# 0
# 1
# 2
# 3
# # 4


# Exemplo 2: Usar while para esperar por uma condição


password = ""
while password != "secret":
    password = input("Enter password: ")
    if password == "secret":
        print("Access granted")
    else:
        print("Try again")

# Saída (depende da entrada do usuário, mas um exemplo seria):
# Enter password: 123
# Try again
# Enter password: secret
# Access granted


# Controle de fluxo em laços:
# Python oferece algumas declarações para alterar o fluxo de execução dentro dos laços: break, continue e else.

# Exemplo 1: Usar break para sair de um laço


for i in range(10):
    if i == 5:
        break
    print(i)

# Saída:
# 0
# 1
# 2
# 3
# 4


# Exemplo 2: Usar continue para pular para a próxima iteração


for i in range(5):
    if i == 2:
        continue
    print(i)

# Saída:
# 0
# 1
# 3
# 4


# Exemplo 3: Usar else com laços


for i in range(5):
    print(i)
else:
    print("Loop finished successfully")

# Saída:
# 0
# 1
# 2
# 3
# 4
# Loop finished successfully


# O bloco else é executado quando o laço termina normalmente (sem ser interrompido por um break).

# Estas são as estruturas de repetição básicas em Python. Compreender como e quando usá-las é fundamental para escrever código eficiente e eficaz.