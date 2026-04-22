n = 18
pilha = []

while n:  # enquanto n é diferente de 0
    pilha.append(n % 2)
    n //= 2

while pilha:
    print(pilha.pop(), end=' ')  # desempilhando
