# função iterativa (utiliza um loop para iterar)
def fatIterativo(n):
    soma = 1
    for i in range(1, n+1):
        soma *= i
    return soma

# função recursiva (chama ela mesma)
def fatRecursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatRecursivo(n-1)
              # 5 * fatRecursivo(5-1) [5*24] = 120
              # 4 * fatRecursivo(4-1) [4*6] ^
              # 3 * faRecursivo(3-1) [3*2] ^
              # 2 * fatRecursivo(2-1) [2*1] ^
              # 1 ^

print(fatIterativo(5))
print(fatRecursivo(5))

# iterativas: mais eficientes, porém mais complexas
# recursivas: mais lentas, porém mais simples de se entender