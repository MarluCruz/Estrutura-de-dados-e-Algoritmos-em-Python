# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:29:29 2022

@author: Admin
"""
def entrada_Gasolina_Velocidade ():
    Tempo = int(input("Quantas horas foram gastas nesta viagem:"))
    Velocidade =int(input("Qual a velócidade média do veículo durante a viagem:"))
    return Tempo, Velocidade

def calculo_da_distancia (Tempo, Velocidade):
    Distancia = Tempo * Velocidade
    return Distancia

def calculo_quantidade_de_litros(Distancia):
        Litros = Distancia / 12
        return Litros
def função_print(Litros):
    print("A Quantidade de litros gasta na viagem foi:", Litros)
    
Tempo_Velocidade = entrada_Gasolina_Velocidade()
Distancia = calculo_da_distancia(Tempo_Velocidade[0], Tempo_Velocidade[1])
Litros = calculo_quantidade_de_litros(Distancia)
função_print(Litros)

