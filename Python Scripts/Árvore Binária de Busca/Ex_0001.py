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
