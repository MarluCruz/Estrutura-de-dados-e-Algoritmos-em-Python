# O(1000) -> O(n)
def lista1():
  lista = []
  for i in range(1000):
    lista += [i]
  return lista
print(lista1())
%timeit lista1()
def lista2():
  return range(1000)
l = lista2()
for i in l:
  print(i)
%timeit lista2()