# 1) Pilha
def valida_expressao(expressao):
    l = []
    for c in expressao:
        if c == ')':
            if l and l[-1] == '(': l.pop()
            else: return False
        elif c == '}':
            if l and l[-1] == '{': l.pop()
            else: return False
        elif c == ']':
            if l and l[-1] == '[': l.pop()
            else: return False
        else:
            l.append(c)
    return len(l) == 0

# 2) Fila
def inverte_fila(deq, k):
    l = []
    for i in range(k):
        l.append(deq.popleft())
    for n in l:
        deq.appendleft(n)
    return deq

# 3) Pilha
class Navegador:
    def __init__(self):
        self.pilha_voltar = []   # Histórico passado
        self.pilha_avancar = []  # Histórico futuro
        self.pagina_atual = None # A aba que você está olhando agora

    def visitar(self, url):
        """Abre uma nova página no navegador."""
        # Se já estivermos em uma página, ela vai para o histórico de "voltar"
        if self.pagina_atual is not None:
            self.pilha_voltar.append(self.pagina_atual)
        
        self.pagina_atual = url
        
        # Dica do desafio: Ao visitar um novo link, o "futuro" é apagado
        self.pilha_avancar.clear() 
        print(f"🌍 Visitando: {self.pagina_atual}")

    def voltar(self):
        """Clica no botão de voltar (Seta para a esquerda)."""
        if not self.pilha_voltar:
            print("⚠️ Fim do histórico. Não é possível voltar.")
            return
        
        # A página atual vai para a pilha de avançar (o "futuro")
        self.pilha_avancar.append(self.pagina_atual)
        
        # Retiramos a última página visitada da pilha de voltar e definimos como atual
        self.pagina_atual = self.pilha_voltar.pop()
        print(f"⬅️ Voltando para: {self.pagina_atual}")

    def avancar(self):
        """Clica no botão de avançar (Seta para a direita)."""
        if not self.pilha_avancar:
            print("⚠️ Não há páginas para avançar.")
            return
        
        # A página atual volta para a pilha de histórico passado
        self.pilha_voltar.append(self.pagina_atual)
        
        # Retiramos a página do topo da pilha de avançar e definimos como atual
        self.pagina_atual = self.pilha_avancar.pop()
        print(f"➡️ Avançando para: {self.pagina_atual}")

    def status(self):
        """Mostra o estado atual das pilhas para fins de depuração."""
        print(f"   [Voltar: {self.pilha_voltar}] | Atual: <{self.pagina_atual}> | [Avançar: {self.pilha_avancar}]\n")