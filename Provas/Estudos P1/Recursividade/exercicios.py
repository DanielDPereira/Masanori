# 1)
# contador_digito(12245, 2) → 2
def contador_digito(n, d):
   if n == 0 and d == 0:
      return 1
   if n == 0:
      return 0
   atual = 1 if (n % 10 == d) else 0
   return atual + contador_digito(n // 10, d)
# 0 + contador_digito(12245 // 10, 2)      0 + 2
# 0 + contador_digito(1224 // 10, 2)       0 + 2
# 1 + contador_digito(122 // 10, 2)        1 + 1
# 1 + contador_digito(12 // 10, 2)         1 + 0
#                 0

# 2)
# is_palindromo('ovo') → True
def is_palindromo(s):
   if len(s) <= 1:
      return True
   if s[0] == s[-1]:
      return is_palindromo(s[1:-1])
   return False

# 3)
# busca_binaria(lista, alvo, inicio, fim)
def busca_binaria(lista, alvo, inicio, fim):
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        return meio
    elif alvo > lista[meio]:
        return busca_binaria(lista, alvo, inicio, meio-1)
    else:
        return busca_binaria(lista, alvo, meio+1, fim)
