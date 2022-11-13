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
        while (atual!= None) and (atual.valor < valor): # um ciclo de repetição percorre a lista até o final ou até achar um número que seja maior que valor
            anterior = atual
            atual = atual.proximo
        novo.proximo = atual
        if anterior != None:
            anterior.proximo = novo
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
                print("Valor não encontrado")
                return None
            else:
                atual = atual.proximo
                return print("O valor encontrado é : ", atual.valor)
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
    def alterarElemento (self, valor1, valor2):
        novo = No(valor2)
        anterior = None
        atual = self.primeiro
        while(atual != None) and (atual.valor != valor1):
            anterior = atual
            atual = atual.proximo
        if (anterior != None):
        
            if (atual != None):
                atual.valor = valor2
                print("Valor Alterado\n")
            else:
                print("Valor não encontrado\n")
        elif atual.valor == valor1:
            atual.valor = valor2
            print("Valor Alterado\n")
        else:
            print("Lista Vazia\n")

        

            
def switch(case,):
    if case == "1":
        print("Qual número você deseja inserir no início?\n")
        valor = input(int())
        return lista.insere_inicio(valor)
    elif case == "2":
        print("Qual número você deseja inserir na Lista?\n")
        valor = input(int())
        return lista.inseriremordem(valor)
    elif case == "3":
        return lista.mostrar()
    elif case == "4":
        print("Qual número você deseja pesquisar?\n")
        valor = input(int())
        return lista.pesquisa(valor)
    elif case == "5":
        return lista.excluir_inicio()
    elif case == "6":
        lista.mostrar()
        print("Qual número você deseja excluir?\n")
        valor = input(int())
        return lista.excluir_posicao(valor)
    elif case == "7":
        lista.mostrar()
        print("Qual elemento da lista exibida acima você deseja mudar\n?")
        valor1 = input(int())
        print("Qual será o novo elemento da Lista?\n")
        valor2 = input(int())
        return lista.alterarElemento(valor1, valor2)
    else:
       print("Entrada inválida. Digite uma entrada válida por favor: \n")
       caSe = input(int())
       switch(caSe)
        

lista = ListaEncadeada()
while True:
    print("Escolha uma das opções:\n")
    print("\n(1) Inserir elemento no inicio da Lista\n ");
    print("(2) Inserir elemento em ordem (verifique se a lista esta ordenada)\n ");
    print("(3) Exibir todos os elementos da Lista\n ");
    print("(4) Realizar uma pesquisa\n ");
    print("(5) Excluir no início da Lista\n ");
    print("(6) Excluir elemento específico da lista\n ");
    print("(7) Alterar elemento da Lista\n ");
    print("(0) Sair\n ");
    case = input(int())
    if case == "0":
        break
    switch(case)