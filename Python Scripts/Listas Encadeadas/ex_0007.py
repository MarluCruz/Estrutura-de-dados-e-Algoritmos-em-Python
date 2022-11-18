#fila com lista encadeada de extremidade dupla
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    def mostrar_no(self):
        print(self.valor)
class ListaEncadeadaDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    def __lista_vazia(self):
        return self.primeiro == None
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        novo.proximo = self.primeiro
        self.primeiro = novo
    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
        self.ultimo = novo
    def excluir_inicio(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return
        temp = self.primeiro
        if self.primeiro.proximo == None:
            self.ultimo = None
        self.primeiro = self.primeiro.proximo
        return temp
    def mostrar(self):
        if self.__lista_vazia():
            print('A lista está vazia')
            return
        atual = self.primeiro
        while atual != None:
            atual.mosta_no()
            atual = atual.proximo
class FilaListaEncadeada:
    def __init__(self):
        self.lista = ListaEncadeadaDupla()
    def enfileirar (self, valor):
        return self.lista.insere_final(valor)
    def desenfileirar (self):
        return self.lista.excluir_inicio()
    def fila_vazia(self):
        return self.lista.__lista_vazia()
    def ver_inicio(self):
        return self.lista.primeiro
def switch (case):
    if case == '1':
        print('Digite o valor que será enfileirado:\n')
        valor = input(float())
        return lista_fila.enfileirar(valor)
    elif case == '2':
        desenfileirado = lista_fila.desenfileirar()
        if desenfileirado == None:
            return None
        else:
            print(desenfileirado.valor, ' Foi desenfileirado')
            return desenfileirado.valor
    elif case == '3':
        return lista_fila.fila_vazia()
    elif case == '4':
        print(lista_fila.ver_inicio)
    else:
        print('Opção inválida digite uma opção válida, por favor:')
        option = input(int())
        if option == "5":
            return "Break"
        switch(option)
lista_fila = FilaListaEncadeada()
while True:
    print('Escolha uma das opções:')
    print('(1) Enfileirar um número.')
    print('(2) Desenfileirar um número.')
    print('(3) Observar se a fila está vazia.')
    print('(4) Obeservar o início da fila.')
    print('(5) Encerrar o programa')
    case = input(int())
    if case == '5':
        break
    else:
         validador= switch(case)
         if validador == "Break":
            break