
# Claro! As estruturas condicionais em Python permitem que o programa tome decisões diferentes com base em certas condições. A estrutura condicional mais comum é o if, que pode ser usada sozinha ou em combinação com elif e else para criar ramificações de decisão mais complexas.

# Aqui estão alguns exemplos práticos:

# 1. Estrutura if
# A estrutura if executa um bloco de código apenas se a condição especificada for verdadeira.


x = 10

if x > 5:
    print("x é maior que 5")  # Saída: x é maior que 5

# 2. Estrutura if-else
# A estrutura if-else fornece uma alternativa: se a condição if não for verdadeira, o bloco else será executado.


x = 3

if x > 5:
    print("x é maior que 5")
else:
    print("x não é maior que 5")  # Saída: x não é maior que 5


# 3. Estrutura if-elif-else
# A estrutura if-elif-else permite testar múltiplas condições. O bloco elif (abreviação de "else if") permite adicionar condições adicionais após um if inicial. O bloco else é opcional e será executado se nenhuma das condições anteriores for verdadeira.


x = 7

if x > 10:
    print("x é maior que 10")
elif x > 5:
    print("x é maior que 5 mas menor ou igual a 10")  # Saída: x é maior que 5 mas menor ou igual a 10
else:
    print("x é menor ou igual a 5")


# 4. Estruturas aninhadas
# Estruturas condicionais podem ser aninhadas dentro de outras estruturas condicionais para criar lógica mais complexa.


x = 8
y = 3

if x > 5:
    if y > 5:
        print("x e y são maiores que 5")
    else:
        print("x é maior que 5, mas y não é")  # Saída: x é maior que 5, mas y não é
else:
    print("x não é maior que 5")


# 5. Operadores lógicos
# Você pode combinar múltiplas condições usando operadores lógicos como and, or e not.


x = 4
y = 6

if x > 2 and y > 5:
    print("x é maior que 2 e y é maior que 5")  # Saída: x é maior que 2 e y é maior que 5

if x > 2 or y > 5:
    print("x é maior que 2 ou y é maior que 5")  # Saída: x é maior que 2 ou y é maior que 5

if not x > 5:
    print("x não é maior que 5")  # Saída: x não é maior que 5


# Exemplo prático completo
# Aqui está um exemplo mais completo que usa várias estruturas condicionais para determinar a categoria de idade de uma pessoa:


idade = 25

if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")  # Saída: Adulto
else:
    print("Idoso")


# Neste exemplo, o programa determina a categoria de idade com base no valor da variável idade. Ele usa if, elif e else para cobrir todas as faixas etárias possíveis.

# Esses exemplos mostram como você pode usar estruturas condicionais em Python para controlar o fluxo de execução do seu programa com base em diferentes condições.