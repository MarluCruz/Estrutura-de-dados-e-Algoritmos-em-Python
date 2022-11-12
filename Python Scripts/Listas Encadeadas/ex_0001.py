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
        atual = self.primeiro # atribui o primeiro elemento da lista
        while atual != None:
            atual.mostra_no() #Printa o primeiro elemento da lista
            atual = atual.proximo #Atribui o próximo elemento da lista

lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.mostrar()
print(lista.primeiro) #Mostra o Primeiro Elemento
print(lista.primeiro.proximo) #Mostra o Segundo Elemento