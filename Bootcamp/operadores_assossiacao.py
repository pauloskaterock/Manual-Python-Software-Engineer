
# Em Python, operadores de associação são usados para verificar a presença de um valor em uma sequência, como listas, tuplas ou strings. Os principais operadores de associação em Python são in e not in.

# Aqui estão alguns exemplos de código que demonstram como usar esses operadores:

# Operador in
# O operador in é usado para verificar se um valor está presente em uma sequência.

# Exemplo 1: Verificando a presença de um elemento em uma lista

fruits = ['apple', 'banana', 'cherry']
print('apple' in fruits)  # Saída: True
print('grape' in fruits)  # Saída: False

# Exemplo 2: Verificando a presença de um caractere em uma string

sentence = "Hello, world!"
print('H' in sentence)  # Saída: True
print('z' in sentence)  # Saída: False

# Exemplo 3: Verificando a presença de uma chave em um dicionário

student = {'name': 'John', 'age': 25, 'grade': 'A'}
print('name' in student)  # Saída: True
print('address' in student)  # Saída: False

# Operador not in
# O operador not in é usado para verificar se um valor não está presente em uma sequência.

# Exemplo 1: Verificando a ausência de um elemento em uma lista

fruits = ['apple', 'banana', 'cherry']
print('grape' not in fruits)  # Saída: True
print('banana' not in fruits)  # Saída: False

# Exemplo 2: Verificando a ausência de um caractere em uma string

sentence = "Hello, world!"
print('z' not in sentence)  # Saída: True
print('H' not in sentence)  # Saída: False

# Exemplo 3: Verificando a ausência de uma chave em um dicionário

student = {'name': 'John', 'age': 25, 'grade': 'A'}
print('address' not in student)  # Saída: True
print('name' not in student)  # Saída: False


# Usos Combinados com Estruturas Condicionais
# Os operadores de associação são frequentemente usados em estruturas condicionais para controlar o fluxo do programa com base na presença ou ausência de valores.

# Exemplo 1: Uso com if-else

colors = ['red', 'pink', 'green']
if 'blue' in colors:
    print("Blue is in the list!")
else:
    print("Blue is not in the list.")
    
# Exemplo 2: Uso em loops

numbers = [1, 2, 3, 4, 5]
for number in range(10):
    if number in numbers:
        print(f"{number} is in the list.")
    else:
        print(f"{number} is not in the list.")
        
        
# Os operadores de associação são poderosos e úteis para verificar rapidamente a presença ou ausência de elementos em sequências, tornando o código mais legível e eficiente.