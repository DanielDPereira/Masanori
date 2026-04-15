# Criando a fila
fila = ["Ana", "Bento", "Carla"]

# Operação de Enfileirar (Enqueue)
fila.append("Daniel")  # Adiciona ao final
print(f"Fila após append: {fila}")

# Operação de Desenfileirar (Dequeue)
primeiro = fila.pop(0)  # Remove o elemento da posição 0
print(f"Pessoa atendida: {primeiro}")
print(f"Fila final: {fila}")