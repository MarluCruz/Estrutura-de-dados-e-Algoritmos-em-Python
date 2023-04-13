#Implementação 4 - Pesquisa Binária
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
    # O(log n)
    def pesquisar_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            # Se achou na primeira tentativa
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            # Se não achou
            elif limite_inferior > limite_superior:
                return -1
            # Divide os limites
            else:
                # Limite inferior
                if self.valores[posicao_atual] < valor :
                    limite_inferior = posicao_atual + 1
                # Limite superior
                else:
                    limite_superior = posicao_atual -1
          
    def excluir(self, valor):
        posicao = self.pesquisar_binaria(valor)
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
vetor.imprime()
vetor.excluir(16)
vetor.imprime()
