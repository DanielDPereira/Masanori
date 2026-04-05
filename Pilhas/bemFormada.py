# uma expressão é bem formada se os parênteses e as chaves fecharem

def BemFormada(s):
    p = []
    for c in s:
        if c == ')':  # se for fechamento de parênteses
            if p[-1] == '(': p.pop()  # se o anterior for a abertura, desempilha
            else: return False
        elif c == '}':  # se for fechamento de chaves
            if p[-1] == '{': p.pop()
            else: return False
        else:  # se for abertura, empilha
            p.append(c)
    return len(p) == 0  # len = 0 significa que todos os parênteses e chaves fecharam
    
print(BemFormada('((){()})'))
print(BemFormada('({)}'))