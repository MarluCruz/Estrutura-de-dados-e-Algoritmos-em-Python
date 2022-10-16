#Comparação de VetorNãoOrdenado vs VetorOrdenado
import numpy as np
import random 

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
                    limite_superior = posicao_atual
          
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

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
    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

def insere_nao_ordenado(lista):
    vetor = VetorNaoOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
    return vetor

def insere_ordenado(lista):
    vetor = VetorOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
        return vetor
def pesquisa_nao_ordenado(lista):
    for i in lista:
        vetor_nao_ordenado.pesquisar(i)

def pesquisa_ordenado_binaria(lista):
    for i in lista:
        vetor_ordenado.pesquisar_binaria(i)

#Inserção
round(random.random(), 4)
elementos = []
for _ in range(10000):
    elementos.append(round(random.random(), 4))
print(len(elementos))
#%timeit insere_nao_ordenado(elementos)
#%timeit insere_ordenado(elementos)

#Pesquisa
vetor_nao_ordenado = insere_nao_ordenado(elementos)
vetor_ordenado = insere_ordenado(elementos)
pesquisa = []
for _ in range(10000):
    pesquisa.append(round(random.random(), 4))
%timeit pesquisa_nao_ordenado(pesquisa)
%timeit pesquisa_ordenado_binaria(pesquisa)