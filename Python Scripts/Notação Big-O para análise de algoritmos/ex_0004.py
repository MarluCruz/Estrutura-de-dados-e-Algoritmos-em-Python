#Funções com notação Big - O
lista = [1, 2, 3, 4, 5]

# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n) -> O(n)
def constant(n):
  print(n[0])
  print(n[1])

def linear(n):
  for i in n:
    print(i)

def quadratic(n):
  for i in n:
    for j in n:
      print(i, j)
    print('---') 

def combination(n):
  # O(1)
  print(n[0])

  # O(5)
  for i in range(5):
    print('test ', i)

  # O(n)
  for i in n:
    print(i)

  # O(n)
  for i in n:
    print(i)

  # O(3)
  print('Python')
  print('Python')
  print('Python')

constant(lista)
linear(lista)
quadratic(lista)
combination(lista)