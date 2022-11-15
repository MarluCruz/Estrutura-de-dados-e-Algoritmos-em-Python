#Pilha com Listas encadeadas
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    def mostrar_no(self):
        print(self.valor)
class ListaEncadeada:
    def __init__(self):
        self.primeiro = None
    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo
    def excluir_inicio(self):
        if self.primeiro == None:
            print('A pilha está vázia')
            return None
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp
    def lista_vazia(self):
        if self.primeiro == None:
            print('A pilha está vazia')
            return None
        else:
            print("A pilha não está vazia")
class PilhaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeada()
    def empilhar(self, valor):
        self.lista.inserir_inicio(valor)
    def desempilhar(self):
        return self.lista.excluir_inicio()
    def pilha_vazia(self):
        return self.lista.lista_vazia()
    def ver_topo(self):
        if self.lista.primeiro == None:
            return -1
        return self.lista.primeiro.valor

def switch (case):
    if case == '1':
        print('Digite o valor que será empilhado:\n')
        valor = input(float())
        return lista_pilha.empilhar(valor)
    elif case == '2':
        desempilhado = lista_pilha.desempilhar()
        if desempilhado == None:
            return None
        else:
            print(desempilhado.valor, ' Foi desempilhado')
            return desempilhado.valor
    elif case == '3':
        return lista_pilha.pilha_vazia()
    elif case == '4':
        print(lista_pilha.ver_topo())
    else:
        print('Opção inválida digite uma opção válida, por favor:')
        option = input(int())
        if option == "5":
            return "Break"
        switch(option)

lista_pilha = PilhaListaEncadeada()

while True:
    print('Escolha uma das opções:')
    print('(1) Empilhar um número.')
    print('(2) Desempilhar um número.')
    print('(3) Observar se a pilha está vazia.')
    print('(4) Obeservar o topo da pilha.')
    print('(5) Encerrar o programa')
    case = input(int())
    if case == '5':
        break
    else:
         validador= switch(case)
         if validador == "Break":
            break