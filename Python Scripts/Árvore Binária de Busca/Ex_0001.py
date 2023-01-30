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
        self.raiz = None #A raiz de uma árvore vazia aponta  valor None
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
                self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor)) #Essa codificação é opcional
                pai.esquerda = None
            else:
                self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor)) #Essa codificação é opcional
                pai.direita = None
        # O nó a ser apagado não possui filho na direita
        elif atual.direita == None:
             #Essa codificação é opcional
            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.esquerda.valor)) 
            #-----------------------------
            if atual == self.raiz:
                self.raiz = atual.esquerda
                
                self.ligacoes.append(str(self.raiz.valor) + '->' + str(atual.esquerda.valor)) #Essa codificação é opcional
            elif e_esquerda == True:
                pai.esquerda = atual.esquerda
                #Essa codificação é opcional
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.esquerda.valor))
            else:
                pai.direita = atual.esquerda
                #Essa codificação é opcional
                self.ligacoes.append(str(pai.valor) +'->'
                + str (atual.esquerda.valor))
        # O nó a ser apagao não possui filho na esquerda
        elif atual.esquerda == None:
             #Essa condição é opcional
            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.direita.valor))
            #_________________________
            if atual == self.raiz:
                self.ligacoes.append(str(self.raiz.valor) + '->' + str(atual.direita.valor)) #Essa condificação é opcional
                self.raiz = atual.direita
            elif e_esquerda == True:
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.direita.valor)) #Essa codificação é opcional
                pai.esquerda = atual.direita
            else:
                self.ligacoes.append(str(pai.valor) + '->' + str(atual.direita.valor))
                pai.direita = atual.direita
        # O nó possui dois filhos
        else:
            sucessor = self.get_sucessor(atual)
            #Esta codificação é opcional
            self.ligacoes.remove(str(pai.valor) + '->' + str(atual.valor))
            self.ligacoes.remove(str(atual.direita.valor) + '->' + str(sucessor.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.esquerda.valor))
            self.ligacoes.remove(str(atual.valor) + '->' + str(atual.direita.valor))
            #__________________________
            if atual == self.raiz:
                self.ligacoes.append(str(self.raiz.valor) + '->' + str(sucessor.valor))#Esta codificação é opcional
                self.raiz = sucessor
            elif e_esquerda == True:
                self.ligacoes.append(str(pai.valor) + '->' + str(sucessor.valor)) #Esta codificação é opcional
                pai.esquerda = sucessor
            else:
                self.ligacoes.append(str(pai.valor) + '->' + str(sucessor.valor))#Esta codificação é opcional
                pai.direita = sucessor
            #Esta codificação é opcional
            self.ligacoes.append(str(sucessor.valor) + '->' + str(atual.esquerda.valor))
            self.ligacoes.append(str(sucessor.valor) + '->' + str(atual.direita.valor))
             #__________________________
            sucessor.esquerda = atual.esquerda
        return True
    def get_sucessor(self, no):
        pai_sucessor = no
        sucessor = no
        atual = no.direita
        while atual != None:
            pai_sucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        if sucessor != no.direita:
            pai_sucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
        return sucessor
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
""""
#Pesquisa
if arvore.pesquisar(72) == None:
    (print('Elemento não localizado'))
else:
    print('Elemento localizado')
"""
#Travessia
arvore.pre_ordem(arvore.raiz)
#arvore.em_ordem(arvore.raiz)
#arvore.no_pos_ordem(arvore.raiz)
#Excluir

#arvore.excluir(72)
#print(arvore.ligacoes)
