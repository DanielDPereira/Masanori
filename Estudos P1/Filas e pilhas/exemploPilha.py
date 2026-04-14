# Criando a pilha
pilha = [10, 20, 30]

# Operação de Empilhar (Push)
pilha.append(40)  # Adiciona ao topo
print(f"Pilha após append: {pilha}")

# Operação de Desempilhar (Pop)
topo = pilha.pop()  # Remove o último elemento
print(f"Elemento removido: {topo}")
print(f"Pilha final: {pilha}")