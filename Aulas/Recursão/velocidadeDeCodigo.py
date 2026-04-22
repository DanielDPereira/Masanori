# seu eu fizer fib(100) usando recursividade, o código levará 5h para executar
#                                     fib(100)
#                    fib(99)                            fib(98)
#         fib(98)            fib(97)            fib(97)          fib(96)
#    fib(97)  fib(96)    fib(96)  fib(95)  fib(96) fib(95)   fib(95)  fib(94)
# observe como o código repete muita coisa ja feita

# melhorando o código
dic = {}
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    if n not in dic: dic[n] = fib(n - 1) + fib(n - 2)
    return dic[n]
print(fib(100))
# so calculo um valor se ele ainda nao esta no dicionario


# melhorando mais ainda
from functools import cache

@cache  # decorador que envelopa a funcao, dando superpoderes
def fib2(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)
print(fib2(100))


# analise as duas funcoes, aparentemente iguais:
def f1(n):
    if n == 1: return 1
    return f1(n - 1) + f1(n - 1)

def f2(n):
    if n == 1: return 1
    return 2 * f2(n - 1)
print(f1(4), f2(4))
# questâo: as duas funcoes sao equivalentes?
# f1(n) é mais lenta, pois repete coisas já feitas