import numpy as np #Lista encadeada simples
class No: # A classe que cria os nós
    def __init__(self, valor): #Função construtora
        self.valor = valor 
        self.proximo = None
    
    def mostra_no(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None #A cabeça da lista quando está vazia aponta para None


    def insere_inicio(self, valor): #Função insere no início
        novo = No(valor) #Um nó é inserido na lista
        novo.proximo = self.primeiro # novo.proximo passa a aponta para o próximo elemento
        self.primeiro = novo #A cabeça passa a apontar para o novo elemento
    def inseriremordem(self, valor):
        novo = No(valor) # O Novo nó é criado
        atual = self.primeiro # A cabeça da lista é atribuída a atual
        anterior = None # Anteriro recebe None
        while (atual!= None) and (atual.proximo < valor): # um ciclo de repetição percorre a lista até o final ou até achar um número que seja maior que valor
            anterior = atual
            atual = atual.proximo
        novo.proximo = atual 
        if anterior != None:
            anterior = novo
        else:
            self.primeiro = novo
    def mostrar(self):
        if self.primeiro == None: #Se o próximo elemento da memória for none retorne none
            print('A lista está vazia')
            return None
        atual = self.primeiro #atribui o primeiro elemento da lista
        print("_________")
        while atual != None:
            atual.mostra_no() #Printa o nó da lista
            atual = atual.proximo #Atribui o próximo elemento da lista
        print("_________")
    def pesquisa (self, valor):
        if self.primeiro == None: #SE a lista estiver fazia retorna None e printa que a lista está vazia
            print('A lista está vazia')
            return None
        atual = self.primeiro #atribui a atual o valor da cabeça da lista
        while atual.valor != valor: #Enquanto o valor de atual for diferente do valor o ciclo continua
            if atual.proximo == None:# Se próximo for None retorna NOne
                return None
            else:
                atual = atual.proximo
        return atual 
    def excluir_inicio(self):
        if self.primeiro == None: #Se o próximo elemento da memória for none retorne none
            print('A lista está vazia')
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp
    def excluir_posicao(self, valor):
        if self.primeiro == None: #SE a lista estiver fazia retorna None e printa que a lista está vazia
            print('A lista está vazia')
            return None
        atual = self.primeiro #atribui a atual o valor da cabeça da lista
        anterior = self.primeiro
        while atual.valor != valor: #Enquanto o valor de atual for diferente do valor o ciclo continua
            if atual.proximo == None:# Se próximo for None retorna NOne
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        return atual

lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.mostrar()
print(lista.primeiro) #Mostra o Primeiro Elemento
print(lista.primeiro.proximo) #Mostra o Segundo Elemento