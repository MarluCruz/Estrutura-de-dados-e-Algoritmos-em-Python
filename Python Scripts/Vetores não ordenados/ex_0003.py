#Implementação 3 - Pesquisa Linear
import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty (self.capacidade, dtype=int)
    
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O Vetor está vazio')
        else:
            for i in range (self.ultima_posicao +1):
                print(i, '-', self.valores[i])
    
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print ("Capacidade Máxima atingida")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
vetor = VetorNaoOrdenado(5)
vetor.insere(2)
vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)
vetor.imprime()
print(vetor.pesquisar(8))
print(vetor.pesquisar(9))
print(vetor.pesquisar(2))