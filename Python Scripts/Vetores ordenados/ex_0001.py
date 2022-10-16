#Implementação 1 - inserção
import numpy as np

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype= int)
    
    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
                print ('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])
    
    #O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade máxima atingida')
            return
        if valor > self.valores[self.ultima_posicao]:
            self.valores[self.ultima_posicao+1] = valor
            self.ultima_posicao += 1
            return
        else:
            posicao = 0
            for i in range (self.ultima_posicao +1):
                posicao = i
                if self.valores[i] > valor:
                    break
            x = self.ultima_posicao
            while x >= posicao:
                self.valores[x+1] =self.valores[x]
                x -= 1
            self.valores[posicao] = valor
            self.ultima_posicao += 1
    
vetor = VetorOrdenado(5)
vetor.insere(8)
vetor.insere(4)
vetor.insere(64)
vetor.insere(32)
vetor.insere(16)
vetor.imprime()
