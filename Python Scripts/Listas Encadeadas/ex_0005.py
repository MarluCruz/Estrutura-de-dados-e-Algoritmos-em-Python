#Lista Duplamente Encadeada
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None
    def mostrar_no(self):
        print(self.valor)
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
    def __lista_vazia(self):
        return self.primeiro == None
    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
        novo.proximo = self.primeiro
        self.primeiro = novo
    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultima
        self.ultimo = novo
    def excluir_inicial(self):
        temp = self.primeiro
        if self.primeiro.proximo == None:
          self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None  
        self.primeiro = self.primeiro.proximo
        return temp
    def mostrar_frente(self):
        atual = self.primeiro
        print("____________")
        while atual != None:
            atual.mostrar_no()
            atual = atual.proximo
        print("____________")
    def mostrar_tras(self):
        atual = self.ultimo
        print("____________")
        while atual != None:
            atual.mostrar_no()
            atual = atual.anterior
        print("____________")
lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(2)
lista.insere_inicio(3)
lista.insere_inicio(4)
lista.insere_inicio(5)
lista.mostrar_frente()
lista.mostrar_tras()