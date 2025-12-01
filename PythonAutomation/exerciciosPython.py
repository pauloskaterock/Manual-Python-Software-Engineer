# 🚀 Desafio de Reforço
# Para garantir que você fixou os conceitos do Capítulo 1, me ajude a escrever um programa que faça o seguinte:

# Pergunte ao usuário o nome dele.

# Pergunte ao usuário o ano de nascimento dele.

# Calcule a idade atual do usuário (assumindo o ano de 2025).

# Exiba uma mensagem formatada com o nome do usuário e a idade calculada.
# ===============================================
# Variável Global (Conceito de Constante)
# ===============================================
# Definimos o ano atual como 2025 (como solicitado no desafio).
# Usamos letras maiúsculas por convenção, indicando que este valor
# não deve ser alterado durante a execução do programa.
ANO_ATUAL = 2025

# ===============================================
# Coletando a Entrada do Usuário (Input)
# ===============================================

# 1. Solicita o nome ao usuário usando a função input().
# O texto digitado pelo usuário será armazenado na variável 'nome_usuario'.
# O valor retornado por input() é sempre do tipo string (texto).
nome_usuario = input("Por favor, digite seu nome: ")

# 2. Solicita o ano de nascimento ao usuário.
# O valor digitado é uma string, e é armazenado temporariamente em 'ano_nascimento_str'.
# Vamos precisar converter este valor para um número para fazer o cálculo.
ano_nascimento_str = input("Em que ano você nasceu? (Ex: 1990): ")

# ===============================================
# Processamento e Conversão de Tipos
# ===============================================

# 3. Conversão de Tipo (Typecasting):
# Usamos a função int() para converter a string (ano_nascimento_str)
# em um número inteiro (int) e armazenamos na variável 'ano_nascimento_int'.
# Essa conversão é essencial para que possamos realizar operações matemáticas.
ano_nascimento_int = int(ano_nascimento_str)

# 4. Cálculo da Idade:
# Realiza a subtração: (Ano Atual - Ano de Nascimento).
# O resultado desta operação é do tipo int (inteiro) e é armazenado em 'idade_atual'.
idade_atual = ANO_ATUAL - ano_nascimento_int

# ===============================================
# Saída Formatada (Output)
# ===============================================

# 5. Exibe a mensagem final para o usuário usando a função print().
# Concatenamos (unimos) strings e variáveis para formar uma mensagem coesa.
# Nota: Podemos usar f-strings (f"...") para tornar a concatenação mais limpa.

# Formatação usando f-string (mais moderna e recomendada):
print(f"\nOlá, {nome_usuario}!")
print(f"Com base no ano {ANO_ATUAL}, sua idade calculada é: {idade_atual} anos.")

# Exemplo de formatação usando vírgulas na função print() (o Python adiciona espaços):
# print("Olá,", nome_usuario, "! Sua idade é:", idade_atual, "anos.")

# ===============================================
# Verificação de Tipo (Opcional, para reforço do aprendizado)
# ===============================================
# Podemos usar a função type() para confirmar os tipos de dados.
# print(type(nome_usuario))        # Deve ser <class 'str'>
# print(type(ano_nascimento_int))  # Deve ser <class 'int'>
# print(type(idade_atual))         # Deve ser <class 'int'>
