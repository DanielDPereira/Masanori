# Faça a seguinte lista de Listas, Dicionários e sort com key=
# Não use o chatgpt, tente fazer sozinho


# Estrututra List Comprehension = [expressao for valor in iteravel if condicao]

# 1) Seja uma lista de inteiros, mostre apenas os números pares usando list comprehension.
pares = [x for x in range(1, 11) if x % 2 == 0]
print(f'1) {pares}')


# 2) Crie uma lista com os quadrados de todos os números pares de 1 a 20 usando list comprehension.
quadradoPares = [x*x for x in range(1, 21) if x % 2 == 0]
print(f'2) {quadradoPares}')


# 3) Dada uma lista de palavras, ordene-a pelo tamanho das palavras em ordem crescente, utilizando sorted() com a cláusula key=.
lista = ['mario', 'carlos', 'ana', 'sofia', 'santiago']
listaEx3 = sorted(lista, key=len)
print(f'3) {listaEx3}')


# 4) Dada uma lista de palavras, ordene-a pelo número de vogais presentes em cada palavra.
lista = ['mario', 'carlos', 'ana', 'sofia', 'santiago']

def contagem(palavra):
    cont = 0
    for letra in palavra:
        if letra in 'aeiou':
            cont += 1
    return cont

listaEx4 = sorted(lista, key=contagem)
print(f'4) {listaEx4}')


# 5) Dada uma lista de palavras, ordene-a pelo último caractere de cada palavra.
lista = ['arroz', 'feijão', 'tomate', 'ovo', 'salada']

listaEx5 = sorted(lista, key=lambda p: p[-1] if p else '')
print(f'5) {listaEx5}')


# 6) Dada uma string, utilize list comprehension para criar uma nova string onde os caracteres aparecem alternando entre maiúsculas e minúsculas.
lista = ['arroz', 'feijão', 'tomate', 'ovo', 'salada']

listaEx6 = [''.join(letra.upper() if i % 2 == 0 else letra.lower() for i, letra in enumerate(palavra)) for palavra in lista]
print(f'6) {listaEx6}')


# 7) Dada uma lista de strings contendo números misturados com letras (por exemplo, "a3b", "z12y", "c1x"), ordene a lista com base no número contido na string.
lista = ['a3b', 'z12y', 'c1x']

def extrairNumero(palavra):
    return int(''.join(letra for letra in palavra if letra.isnumeric()))

listaEx7 = sorted(lista, key=extrairNumero)
print(f'7) {listaEx7}')



# Estrutura Dictionary Comprehension = {chave: expressão for chave, valor in iterável}
# OBS: se o iterável não for o dicionário, eu não preciso usar dois valores no for

# 8) Crie um dicionário que mapeia os números de 1 a 10 para seus respectivos quadrados, usando dict comprehension.
dictEx8 = {num: num**2 for num in range(1, 11)}
print(f'8) {dictEx8}')


# 9) Dada uma string, crie um dicionário onde as chaves são os caracteres e os valores são a contagem de vezes que cada caractere aparece.
palavra = 'abccdeeea'
dictEx9 = {letra: palavra.count(letra) for letra in palavra}
print(f'9) {dictEx9}')


# 10) Dado um dicionário qualquer, crie um novo dicionário onde as chaves e os valores estejam invertidos.
dicionario = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
dictEx10 = {valor: chave for chave, valor in dicionario.items()}
print(f'10) {dictEx10}')


# 11) Dado um dicionário de números, crie um novo dicionário contendo apenas os pares chave-valor onde o valor seja maior que um determinado número.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dictEx11 = {chave: valor for chave, valor in dicionario.items() if valor > 3}
print(f'11) {dictEx11}')


# 12) Dado um dicionário, ordene-o pelos valores.
dicionario = {'a': 10, 'b': 2, 'c': 5, 'd': 3}
dictEx12 = {chave: valor for chave, valor in sorted(dicionario.items(), key=lambda item: item[1])}
print(f'12) {dictEx12}')


# 13) Dado um dicionário onde as chaves são palavras, ordene-o com base no comprimento das chaves.
dicionario = {'ab': 2, 'abcd': 4, 'a': 1, 'abc': 3}
dictEx13 = {chave: valor for chave, valor in sorted(dicionario.items(), key=lambda item: len(item[0]))}
print(f'13) {dictEx13}')


# 14) Dada uma frase, crie um dicionário onde as chaves são palavras e os valores são a contagem de vezes que cada palavra aparece.
palavras = 'dois tres dois um tres tres'
dictEx14 = {palavra: palavras.count(palavra) for palavra in palavras.split()}
print(f'14) {dictEx14}')


# 15) Dado um dicionário onde os valores são números, crie um novo dicionário onde cada valor seja a raiz quadrada do original.
dicionario = {'a': 25, 'b': 64, 'c': 81, 'd': 144}
dictEx15 = {chave: int(valor**0.5) for chave, valor in dicionario.items()}
print(f'15) {dictEx15}')


# 16) Dada uma lista de palavras, crie um dicionário onde as chaves sejam as primeiras letras e os valores sejam listas das palavras correspondentes.
# lista = 'cax abe b13 c23 arr d12'.split()
# saída: {'a': ['abe', 'arr'], 'b':['b13'], 'c':['cax', 'c23'], 'd': ['d12']}
lista = 'cax abe b13 c23 arr d12'.split()

def acharInicial(lista):
    dictEx16 = {}
    for p in sorted(lista):
        # if dictEx16.get(p[0]):
        #     dictEx16[p[0]].append(p)
        # else:
        #     dictEx16[p[0]] = []
        #     dictEx16[p[0]].append(p)
        dictEx16.setdefault(p[0], []).append(p)
    return dictEx16

print(f'16) {acharInicial(lista)}')