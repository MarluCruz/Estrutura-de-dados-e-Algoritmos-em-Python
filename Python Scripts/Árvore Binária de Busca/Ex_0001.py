#Árvore Binária de Busca
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    def mostra_no(self):
        print(self.valor)
class ArvoreBinarariaBusca:
    def __init__(self):
        self.raiz = None #A raiz de uma árvore vazia aponta para tem valor None
        self.ligacoes = []
    def inserir(self, valor):
        novo = No(valor)
        # Se a árfore estiver vazia
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                # Esquerda
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return
                # Direita
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        self.ligacoes.append(str(pai.valor) + '->' + str(novo.valor))
                        return
    def pesquisar(self,valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita
            if atual == None:
                return None
        return atual
        # Raiz, esquerda, direita
    def pre_ordem(self, no):
        if no != None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)
    # Esquerda, raiz, direita
    def em_ordem(self, no):
        if no != None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)
    def no_pos_ordem(self, no):
        if no != None:
            self.no_pos_ordem(no.esquerda)
            self.no_pos_ordem(no.direita)
            print(no.valor)
    def excluir(self, valor):
        if self.raiz == None:
            print('A arvore está vazia')
            return
        #Encontrar o nó
        atual = self.raiz
        pai = self.raiz
        e_esquerda = True
        while atual.valor != valor:
            pai = atual
            #Esquerda
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            #Direita
            if valor > atual.valor:
                e_esquerda = False
                atual = atual.direita
            if atual == None:
                return None
        # O nó a ser apagado é uma folha
        if (atual.esquerda == None) and (atual.direita == None):
            if atual == self.raiz:
                self.raiz == None
            elif e_esquerda == True:
                pai.esquerda = None
            else:
                pai.direita = None   
#Inserção e visualização:
arvore = ArvoreBinarariaBusca()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(71)
arvore.inserir(84)
arvore.inserir(79)
print(arvore.raiz.esquerda.valor)
print(arvore.raiz.direita.valor)
print(arvore.ligacoes)
#Pesquisa
if arvore.pesquisar(72) == None:
    (print('Elemento não localizado'))
else:
    print('Elemento localizado')

#Travessia
arvore.pre_ordem(arvore.raiz)
arvore.em_ordem(arvore.raiz)
arvore.no_pos_ordem(arvore.raiz)