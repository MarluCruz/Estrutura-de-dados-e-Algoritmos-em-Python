#Primeiro exercício de EStruta de dados unijorge
from re import S
import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.array(self.capacidade, dtype = str)
   
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O Vetor está vazio')
        else:
            for i in range (self.ultima_posicao +1):
                print(i, '-', self.valores[i])
    def imprime_lista(self, nomes):
        if self.ultima_posicao == -1:
            print('O Vetor está vazio')
        else:
            arr = np.array(nomes)
            for i in range (len(self.valores)):
                print(arr[i], self.valores[i])
    
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print ("Capacidade Máxima atingida")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor
    
    def insere_list(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print ("Capacidade Máxima atingida")
        else:
            self.ultima_posicao += 1
            arr = np.array(valor)
            self.valores = arr
    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

Valores = VetorNaoOrdenado(50)
Nomes = VetorNaoOrdenado(50)
Codigo = ''
Mercadoria = ''
Quantidade = ''
Preco_Unitario = ''
Preco_Total = ''
valores = []
nomes = []

for i in range(1,50):
    valores.clear()
    nomes.clear()
    Codigo =str(input("Digite um  código para a mercadoria:"))
    Mercadoria = str(input("Digite o nome da mercadoria:"))
    Conversor1 = int (input("Digite a quantidade do produto:"))
    Conversor2 = float(input("Digite o Preço Unitario da Mercadoria:"))
    Quantidade = str(Conversor1)
    Preco_Unitario = str(Conversor2)
    Preco_Total = str(Conversor1 * Conversor2)
    if Conversor1 >= 100:
        valores = [Codigo, Mercadoria, Quantidade, Preco_Unitario, Preco_Total]
        nomes = ['Código:', 'Mercadoria:', 'Quantidade:', 'Preço Unitário,:', 'Preço Total:']
        Valores.insere_list(valores)
        Nomes.insere_list(nomes)
        Valores.imprime_lista(nomes)


#for i in range(len(nomes)):
    #print(nomes[i], valores[i])
   

#print(Codigo)
#print(Mercadoria)
#print(Quantidade)
#print(Preco_Unitario)
#print(Preco_Total)
