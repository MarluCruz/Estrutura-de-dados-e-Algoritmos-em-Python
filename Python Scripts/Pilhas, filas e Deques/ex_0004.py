#Fila Circular
import numpy as np
class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade #Quantos elementos podem ser colocados na fila
        self.inicio = 0 #Marca o início da fila
        self.final = -1 #Marca o final da fila
        self.numeros_elementos = 0 #Quantidade de elementos que existem na fila no momento
        self.valores = np.empty(self.capacidade, dtype = int) #Vetor onde os dados da fila serão armazenados.
    def __fila_vazia(self):#Função para verificar se a fila está vazia
        return self.numeros_elementos == 0
    def __fila_cheia(self):#Função para verirficar se a fila está cheia
        return self.numeros_elementos == self.capacidade
    def enfileirar(self, valor): #Função para adicionar elementos na fila.
        if self.__fila_cheia():
            print('A fila está cheia')
            return 
        if self.final == self.capacidade - 1: #Caso o final já tenha alcançado o último índice do vetor. O que obrigará um ídice a ser desenfileirado e final ser alocado para o índice 0.
            self.final = -1
        self.final += 1
        self.valores [self.final] = valor
        self.numeros_elementos +=1
    def desinfileirar(self):
        if self.__fila_vazia():
            print('A fila já está vazia')
            return
        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade:# Quando o ínicio alcançou o último ídice do vetor. O próximo item a ocupar o ínico será alocado para o ídice 0 novamente.
            self.inicio = 0
        self.numeros_elementos -= 1
        return temp
    def primeiro(self):
        if self.__fila_vazia(): # Mostra o primeiro elemento da fila.
            return-1
        return self.valores[self.inicio]

fila = FilaCircular(5)
print(fila.primeiro())
fila.enfileirar(1)
fila.enfileirar(2)
print(fila.primeiro())
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
fila.enfileirar(6)
fila.desinfileirar()
fila.desinfileirar()
print(fila.primeiro())
fila.enfileirar(6)
fila.enfileirar(7)
print(fila.primeiro())
print(fila.valores)
print(fila.inicio, fila.final)
print(fila.valores[fila.final])
print(fila.valores[fila.inicio])
