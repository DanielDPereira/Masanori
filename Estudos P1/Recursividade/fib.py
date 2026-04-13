# iterativa
def fibI(n):
    a, b = 0, 1
    c = 0
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c

def fibR(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibR(n-1) + fibR(n-2)
#          fibR(3-1)      +      fibR(3-2)
#   fibR(2-1) + fibR(2-2)           1
#       1     +     0          

print(fibI(3))
print(fibR(3))
