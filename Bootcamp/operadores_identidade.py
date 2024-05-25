
# Operadores de identidade em Python são usados para comparar objetos e determinar se eles ocupam a mesma localização na memória. Os dois operadores de identidade em Python são is e is not.

# Operador is
# O operador is verifica se duas variáveis apontam para o mesmo objeto na memória. Ele retorna True se ambas as variáveis são o mesmo objeto e False caso contrário.


a = [1, 2, 3]
b = a
c = [1, 2, 3]

# a e b referenciam o mesmo objeto
print(a is b)  # True

# a e c são objetos diferentes com o mesmo valor
print(a is c)  # False

# Comparação direta com um valor
d = None
print(d is None)  # True

# ---------------------------------------------------------------------------------------
# Operador is not
# O operador is not é o oposto de is. Ele retorna True se duas variáveis não apontam para o mesmo objeto na memória.


x = [4, 5, 6]
y = [4, 5, 6]
z = x

# x e y são objetos diferentes com o mesmo valor
print(x is not y)  # True

# x e z referenciam o mesmo objeto
print(x is not z)  # False

# Comparação direta com um valor
w = None
# print(w is not None)  # False

# Casos comuns de uso
# Os operadores de identidade são frequentemente usados para verificar se uma variável é None, que é uma maneira comum de verificar se uma variável foi inicializada ou se uma condição foi satisfeita.


# def func(param=None):
#     if param is None:
#         param = []
#     param.append(1)
#     return param

# # Chamando a função sem argumentos
# print(func())  # [1]

# # Chamando a função com uma lista
# print(func([2, 3]))  # [2, 3, 1]


# Diferença entre is e ==

# is verifica se duas variáveis referenciam o mesmo objeto.
# == verifica se os valores dos objetos são iguais.


# a = [7, 8, 9]
# b = a
# c = [7, 8, 9]

# # a e b referenciam o mesmo objeto
# print(a is b)  # True
# print(a == b)  # True

# # a e c são objetos diferentes com o mesmo valor
# print(a is c)  # False
# print(a == c)  # True


# Resumo
# Os operadores is e is not são ferramentas úteis em Python para verificar a identidade de objetos, ou seja, se duas variáveis referenciam o mesmo local na memória. Eles são especialmente úteis em verificações contra None e ao lidar com objetos mutáveis como listas e dicionários.