# As classes str em Python são usadas para representar sequências de caracteres (strings). As strings em Python são imutáveis, o que significa que uma vez criadas, elas não podem ser modificadas. Python fornece uma variedade de métodos integrados para manipular e operar em strings.

# Aqui estão alguns exemplos práticos de como trabalhar com strings em Python:

# Criação de Strings:

# Strings podem ser criadas usando aspas simples ou duplas
s1 = 'Hello, World!'
s2 = "Hello, Python!"

print(s1)  # Saída: Hello, World!
print(s2)  # Saída: Hello, Python!


# Concatenando Strings:

# Usando o operador +
s1 = 'Hello'
s2 = 'World'
s3 = s1 + ', ' + s2 + '!'
print(s3)  # Saída: Hello, World!


# Acessando Caracteres em uma String:

s = 'Python'

# Acessando caracteres individuais
print(s[0])  # Saída: P
print(s[1])  # Saída: y

# Acessando caracteres de trás para frente
print(s[-1])  # Saída: n
print(s[-2])  # Saída: o


# Fatiamento de Strings:

s = 'Hello, World!'

# Fatiamento básico
print(s[0:5])   # Saída: Hello
print(s[7:12])  # Saída: World

# Fatiamento com passos
print(s[::2])  # Saída: Hlo ol!
print(s[::-1]) # Saída: !dlroW ,olleH


# Métodos de Strings:

s = '  Hello, World!  '

# Remover espaços em branco das extremidades
print(s.strip())  # Saída: Hello, World!

# Converter para maiúsculas e minúsculas
print(s.upper())  # Saída: HELLO, WORLD!
print(s.lower())  # Saída: hello, world!

# Substituir substrings
print(s.replace('World', 'Python'))  # Saída:   Hello, Python!  

# Encontrar a posição de uma substring
print(s.find('World'))  # Saída: 8

# Dividir uma string em uma lista
print(s.split(','))  # Saída: ['  Hello', ' World!  ']


# Formatando Strings:

name = 'Alice'
age = 30

# Usando o operador % (antigo estilo)
print('My name is %s and I am %d years old.' % (name, age))

# Usando o método format
print('My name is {} and I am {} years old.'.format(name, age))

# Usando f-strings (Python 3.6+)
print(f'My name is {name} and I am {age} years old.')


# Verificando Propriedades de Strings:

s = 'Hello123'

# Verificar se todos os caracteres são alfanuméricos
print(s.isalnum())  # Saída: True

# Verificar se todos os caracteres são letras
print(s.isalpha())  # Saída: False

# Verificar se todos os caracteres são dígitos
print(s.isdigit())  # Saída: False

# Verificar se a string está em minúsculas
print(s.islower())  # Saída: False

# Verificar se a string está em maiúsculas
print(s.isupper())  # Saída: False


# Esses exemplos cobrem muitos dos usos comuns de strings em Python. As strings são um tipo de dado fundamental e são usadas extensivamente em qualquer programa Python, por isso é importante entender como trabalhar com elas de maneira eficaz.