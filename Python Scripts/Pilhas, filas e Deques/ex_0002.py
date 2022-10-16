import numpy as np

class Pilha:
    def __init__(self,capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=str)
    
    def Pilha_cheia(self):
        if self.__topo == self.__capacidade -1:
            return True
        else:
            return False
    
    def Pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False
    
    def empilhar(self, valor):
        if self.Pilha_cheia():
            print('A pilha está cheia')
        else:
            self.__topo +=1
            self.__valores[self.__topo] = valor
            
    def desempilhar(self):
        if self.Pilha_vazia():
            print('A pilha está vazia')
        else:
            for _ in range(1,3):
                self.__valores = np.delete(self.__valores, [self.__topo])
                self.__topo -= 1
        
    def ver_topo(self):
        if self.__topo != -1:
         return self.__valores[self.__topo]
    
    def interagindo_topo(self):
        if self.__topo != -1:
            topo = self.__valores[self.__topo]
            return topo

pilha1 = Pilha(10)
for i in range(1,11):
    caractere = str(input("Digite um caracter válido para construção de uma expressão, como letras ou '()', '{}' '[]':"))
    if ((caractere == '}') or (caractere ==']') or (caractere ==')')) and (pilha1.Pilha_vazia() == True): # Caso a pilha esteja vazia
        caractere = str(input('Caractere inválido, para usar o fechamento de chaves, parênteses ou colchetes é necessários abrí-los primeiro. Digite um caracter válido, por favor:'))
        while ((caractere == '}') or (caractere ==']') or (caractere ==')')):
            caractere = str(input('Caracter inválido, para usar 0 fechamento de chaves, parênteses ou colchetes é necessários abrí-los primeiro. Digite um caracter válido, por favor:'))
    else:
        if ((caractere == '{') or (caractere =='[') or (caractere =='(')): 
            pilha1.empilhar(caractere)
        elif caractere == '}': # Controle }
            topo = pilha1.interagindo_topo()
            if topo == '{':
                pilha1.empilhar(caractere)
                topo = pilha1.interagindo_topo()
                if topo == "}":
                    pilha1.desempilhar() 
            else:
                caractere = str(input('Caracter inválido, caso deseje fechar alguma expresão digite:"}"'))
                while (caractere ==']') or (caractere ==')'):
                    caractere = str(input('Caracter inválido, caso deseje fechar alguma expresão digite:"}"'))
                topo = pilha1.interagindo_topo()
                if topo == "}":
                    pilha1.desempilhar()       
        elif caractere == ']': # Controle ]
            topo = pilha1.interagindo_topo()
            if topo == '[':
                pilha1.empilhar(caractere)
                topo = pilha1.interagindo_topo()
                if topo == "]":
                    pilha1.desempilhar() 
            else:
                caractere = str(input('Caracter inválido, caso deseje fechar alguma expresão digite:"]"'))
                while (caractere =='}') or (caractere ==')'):
                    caractere = str(input('Caracter inválido, caso deseje fechar alguma expresão digite:"]"')) 
        elif caractere == ')': # Controle )
            topo = pilha1.interagindo_topo()
            if topo == '(':
                pilha1.empilhar(caractere)
                topo = pilha1.interagindo_topo()
                if topo == "]":
                    pilha1.desempilhar() 
            else:
                caractere = str(input('Caracter inválido, caso deseje fechar alguma expresão digite:")"'))
                while (caractere =='}') or (caractere ==']'):
                    caractere = str(input('Caracter inválido, caso deseje fechar alguma expresão digite:")"'))
                topo = pilha1.interagindo_topo()
                if topo == ")":
                    pilha1.desempilhar()