#Exercício
import numpy as np
import random

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.ultima_posicao = -1
        self.valores = np.empty (self.capacidade, dtype=float)
    
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

    def bubble_sort(self):
        n = self.ultima_posicao + 1

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.valores[j] > self.valores[j + 1]:
                    temp = self.valores[j]
                    self.valores[j] = self.valores[j+1]
                    self.valores[j+1] = temp

    def selection_sort(self):
        n = self.ultima_posicao + 1

        for i in range(n):
            id_minimo = i
            for j in range(i + 1, n):
                if self.valores[id_minimo] > self.valores[j]:
                    id_minimo = j
            temp = self.valores[i]
            self.valores[i] = self.valores[id_minimo]
            self.valores[id_minimo] = temp

    def insertion_sort(self):
        n = self.ultima_posicao + 1

        for i in range(1,n):
            marcado = self.valores[i]

            j = i -1
            while j >= 0 and marcado < self.valores[j]:
                self.valores[j + 1] = self.valores[j]
                j -= 1
                self.valores[j + 1] = marcado
    
    def shell_sort(self):
        intervalo = (self.ultima_posicao + 1) // 2

        while intervalo > 0:
            for i in range(intervalo, self.ultima_posicao + 1):
                temp = self.valores[i]
                j = i
                while j >= intervalo and self.valores [j - intervalo] > temp:
                    self.valores[j] = self.valores[j - intervalo]
                    j -= intervalo
                self.valores[j] = temp
            intervalo //= 2

    def merge_sort(self):
        if self.ultima_posicao + 1 > 1:
            divisao = (self.ultima_posicao +1) // 2
            esquerda = self.valores[:divisao].copy()
            direita = self.valores[divisao:].copy()

            self.__Merge_Sort(esquerda)
            self.__Merge_Sort(direita)

            i = j = k = 0

            # Ordena esquerda e direita
            while i < len(esquerda) and j < len(direita):
                if esquerda[i] < direita[j]:
                    self.valores[k] = esquerda[i]
                    i += 1
                else:
                    self.valores[k] = direita[j]
                    j += 1
                k += 1

            # Ordenação final
            while i < len(esquerda):
                self.valores[k] = esquerda[i]
                i += 1
                k += 1
            while j < len(direita):
                self.valores[k] = direita[j]
                j += 1
                k += 1

    def __Merge_Sort(self, vetor):
        if len(vetor) > 1:
            divisao = len(vetor) // 2
            esquerda = vetor[:divisao].copy()
            direita = vetor[divisao:].copy()

            self.__Merge_Sort(esquerda)
            self.__Merge_Sort(direita)

            i = j = k = 0

            # Ordena esquerda e direita
            while i < len(esquerda) and j < len(direita):
                if esquerda[i] < direita[j]:
                    vetor[k] = esquerda[i]
                    i += 1
                else:
                    vetor[k] = direita[j]
                    j += 1
                k += 1

            # Ordenação final
            while i < len(esquerda):
                vetor[k] = esquerda[i]
                i += 1
                k += 1
            while j < len(direita):
                vetor[k] = direita[j]
                j += 1
                k += 1
        return vetor
    def __particao(self, inicio, final):
        pivo = self.valores[final]
        i = inicio - 1

        for j in range(inicio, final):
            if self.valores[j] <= pivo:
                i += 1
                self.valores[i], self.valores[j] = self.valores[j], self.valores[i]
        self.valores[i + 1], self.valores[final] = self.valores[final], self.valores[i + 1]
        return i + 1
    def quick_sort(self, inicio, final):
        if inicio < final:
            posicao = self.__particao(inicio, final)
            # Esquerda
            self.quick_sort(inicio, posicao - 1)
            # Direito
            self.quick_sort(posicao + 1, final)

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

vetor = VetorNaoOrdenado(600)
vetorOrdenado = VetorOrdenado(600)
round(random.random(), 4)
for i in range(0, 299):
    vetor.insere(round(random.random(), 4))
    vetorOrdenado.insere(vetor.valores[i])

vetor1, vetor2, vetor3, vetor4, vetor5, vetor6 = vetor, vetor, vetor, vetor, vetor, vetor
vetor1.bubble_sort()
vetor2.selection_sort()
vetor3.insertion_sort()
vetor4.shell_sort()
vetor5.merge_sort()
vetor6.quick_sort(vetor6.inicio, vetor6.ultima_posicao)

