# 11 passos
#O comando timeit só funciona no Google collab

from timeit import timeit

def soma1(n):
  soma = 0
  for i in range(n + 1):
    soma += i
  
  return soma
soma1(10)
%timeit soma1(10)

# 3 passos
# O(3)
def soma2(n):
  return (n * (n + 1)) / 2
soma2(10)
%timeit soma2(10)
