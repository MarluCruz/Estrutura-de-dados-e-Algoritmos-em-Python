#Recursão
def soma1(n):
    soma = 0
    for i in range(n +1):
        soma += i
    return soma

def soma2(n):
    if n == 0:
        return 0
    
    return n + soma2(n - 1)

print(soma1(5))
print(soma2(5))

%timeit soma1(100)
%timeit soma2(100)