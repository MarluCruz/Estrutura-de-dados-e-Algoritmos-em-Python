#Fila Circular
import numpy as np
class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade #Quantos elementos podem ser colocados na fila
        self.numeros_elementos = 0 #Quantidade de elementos que existem na fila no momento
        self.valores = np.empty(self.capacidade, dtype = int) #Vetor onde os dados da fila serão armazenados.
    def __fila_vazia(self):#Função para verificar se a fila está vazia
        return self.numeros_elementos == 0
    def __fila_cheia(self):#Função para verirficar se a fila está cheia
        return self.numeros_elementos == self.capacidade
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return
        
        if self.numeros_elementos == 0:
            self.valores[self.numeros_elementos] = valor
            self.numeros_elementos += 1
        else:
            x = self.numeros_elementos -1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                x -= 1
            self.valores[x + 1] = valor
            self.numeros_elementos += 1
    def desenfilerar(self):
        if self.__fila_vazia():
            print('A fila está vazia')
            return
        valor = self.valores[self.numeros_elementos - 1]
        self.numeros_elementos -= 1
        return valor
    def primeiro(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.numeros_elementos -1]

fila = FilaPrioridade(5)
fila.enfileirar(30)
fila.enfileirar(50)
print(fila.primeiro())
fila.enfileirar(10)
print(fila.primeiro())
fila.enfileirar(40)
fila.enfileirar(20)
print(fila.valores)
fila.desenfilerar()
print(fila.primeiro())
fila.desenfilerar()
print(fila.primeiro())
print(fila.valores)
fila.enfileirar(5)
print(fila.valores)