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
    def mostrar(self):
        if self.primeiro == None: #Se o próximo elemento da memória for none retorne none
            print('A lista está vazia')
            return None
        atual = self.primeiro #atribui o primeiro elemento da lista
        while atual != None:
            atual.mostra_no() #Printa o nó da lista
            atual = atual.proximo #Atribui o próximo elemento da lista
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
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)

lista.mostrar()
print(lista.primeiro) #Mostra o endereço de memória do Primeiro Elemento
print(lista.primeiro.proximo) #Mostra o endereço de memória do Segundo Elemento
lista.excluir_posicao(3)
lista.mostrar()
lista.excluir_posicao(1)
lista.mostrar()
lista.excluir_posicao(5)
lista.mostrar()


""""
pesquisa = lista.pesquisa(10)

if pesquisa != None:
    print('Encontrado: ', pesquisa.valor)
else:
    print('Não encontrado')
lista.excluir_inicio()
lista.mostrar()
lista.excluir_inicio()
lista.mostrar()
lista.excluir_inicio()
lista.mostrar()
lista.excluir_inicio()
lista.mostrar()
lista.excluir_inicio()
lista.mostrar()
"""