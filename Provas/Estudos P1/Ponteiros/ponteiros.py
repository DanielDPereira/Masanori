x = 10
y = x
x = 15
print(x, y)
# python só passa por referência, por isso x = y dá no mesmo endereço de memória
# x = 15 não muda o valor no endereço para qual x aponta, mas cria um novo espaço na memória, colocando o 15 e mudando para onde x aponta

x = [10, 15]
y = x
y[0] = 15
print(x, y)
# inteiros são imutáveis, listas são mutáveis

i = 2
j = 2
print(id(i) == id(j))

n1 = 5
n2 = 5
print(n1 is n2)
