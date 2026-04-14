# 1) def inv(s):        inv('abacate') -> 'etacaba'
def inv(s):
    if len(s) <= 1: 
        return s
    return s[-1] + inv(s[:-1])
print(inv('abacate'))
# s = e + inv(abacat)   etacaba
# s = t + inv(abaca)    tacaba     ^
# s = a + inv(abac)     acaba 
# s = c + inv(aba)      caba       ^
# s = a + inv(ab)       aba
# s = b + inv(a)        ba         ^
# s = a

# 2) def sd(n):         sd(123) -> 1 + 2 + 3 -> 6
def sd(n):
    if n <= 9: return n
    return n % 10 + sd(n // 10)
print(sd(123))
# 123 % 10 + sd(123 // 10)   3 + 3
# 12 % 10 + sd(12 // 10)     3 + 1
#                1

# 3) def fib(n):        fib(3) -> 2
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)
print(fib(10))

# 4) def mdc(a, b):     mdc(21, 15) -> 3
def mdc(a, b):
    if b == 0: 
        return a
    return mdc(b, a % b)
print(mdc(21, 15))
# mdc(15, 21 % 15)   3
# mdc(6, 15 % 6)     3
# mdc(3, 6 % 3)      3
# 3

# 5) def dec2bin(n):    dec2bin(18) -> '10010'
def dec2bin(n):
    if n == 0: return '0'
    if n == 1: return '1'
    return dec2bin(n // 2) + str(n % 2)
print(dec2bin(18))
# dec2bin(18 // 2) + '18 % 2'   '1001'+ '0'
# dec2bin(9 // 2) + '9 % 2'     '100' + '1'
# dec2bin(4 // 2) + '4 % 2'     '10' + '0'
# dec2bin(2 // 2) + '2 % 2'     '1' + '0'
# '1'
