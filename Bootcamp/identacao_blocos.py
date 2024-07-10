# A indentação em Python é uma parte crucial da linguagem e é usada para definir a estrutura dos blocos de código, ao contrário de outras linguagens que usam chaves {} ou palavras-chave específicas. Em Python, a indentação indica o início e o fim de blocos de código, como os corpos de funções, loops e condicionais.

# Aqui está um exemplo para ilustrar como a indentação funciona em Python:

# Condicionais:

x = 10

if x > 5:
    print("x é maior que 5")  # Este bloco será executado porque a condição é verdadeira
else:
    print("x é menor ou igual a 5")  # Este bloco não será executado


# No exemplo acima, a linha print("x é maior que 5") está indentada para indicar que ela faz parte do bloco if. Se a condição x > 5 for verdadeira, essa linha será executada.

# Loops:

for i in range(5):
    print(i)  # Este bloco será executado cinco vezes, uma vez para cada valor de i
    if i == 2:
        print("i é igual a 2")  # Este bloco será executado apenas quando i for igual a 2


# Aqui, o bloco de código dentro do loop for está indentado para indicar que ele faz parte do loop. Além disso, o bloco if está ainda mais indentado para mostrar que ele está dentro do bloco for.

# Funções:

def saudacao(nome):
    print(f"Olá, {nome}!")  # Este bloco faz parte da função saudacao

saudacao("João")  # Chama a função saudacao com o argumento "João"

# No exemplo acima, o bloco de código print(f"Olá, {nome}!") está indentado para mostrar que ele pertence à função saudacao.

# Exemplo Prático:
# Aqui está um exemplo mais complexo que combina condicionais, loops e funções para mostrar como a indentação é usada para definir a estrutura do código:


def classificar_numeros(numeros):
    pares = []
    impares = []
    
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)  # Este bloco adiciona números pares à lista pares
        else:
            impares.append(numero)  # Este bloco adiciona números ímpares à lista impares
    
    return pares, impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = classificar_numeros(numeros)

print("Números pares:", pares)
print("Números ímpares:", impares)


# Neste exemplo, a função classificar_numeros classifica uma lista de números em pares e ímpares. Os blocos de código dentro do loop for e do condicional if são indentados para mostrar claramente a estrutura do código e a lógica de fluxo.

# A indentação em Python não é apenas uma questão de estilo, mas uma exigência sintática. Se a indentação não for consistente, o interpretador Python gerará um erro de sintaxe. Portanto, é importante usar um estilo de indentação consistente (geralmente 4 espaços) para garantir que o código seja legível e executável.