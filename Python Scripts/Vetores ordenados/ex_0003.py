#Implementação 3 - Exclusão
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
    # O(n)
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
    # O(n)
    def pesquisar(self, valor):
        for i in range (self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            if i == self.ultima_posicao:
                return -1
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

vetor = VetorOrdenado(10)
vetor.insere(8)
vetor.insere(4)
vetor.insere(64)
vetor.insere(32)
vetor.insere(16)
print(vetor.pesquisar(3))
print(vetor.pesquisar(65))
vetor.excluir(32)
vetor.imprime()