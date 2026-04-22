# estrutura:
# def funcao(argumentos):
#     if base (que eu já sei o resultado, para impedir um loop infinito)
#     return chamando a própria funcao

def fat(n):
    if n == 0 or n == 1: return 1
    return n * fat(n - 1)

print(fat(3))

# teste de mesa:
# n = 3
# --------------
# if 3 == 0 or 3 == 1       3 * 2 = 6
# return 3 * fat(2)
# --------------
#                               ^
# n = 2
# --------------
# if 2 == 0 or 2 == 1       2 * 1 = 2
# return 2 * fat(1)
# --------------
#                               ^
# n = 1
# --------------
# if 1 == 0 or 1 == 1           1
# return 1
# --------------

