a = [1, 2, 3]
b = a

a[0] = 'abacate'

# b também vai mudar pois são os mesmos ponteiros

id(a)
id(b)
# o resultado será o mesmo ID


a = [1, 2, 3]
b = list(a)
a[0] = 42
# agora os resultados serão diferentes
# esou usando um conceito de POO (método construtor) para ter dois objetos diferentes na memória


# EM PYTHON, TUDO É PONTEIRO

