# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:35:46 2022

@author: Admin
"""

h = float(input("Digite o total de horas gasto na viagem:"))
m = float(input("Caso seja necessário, digite quantos minutos foram gastos na viagem:"))
m= (m/60)
t=(h+m)
velocidade = float(input("Qual foi a velocidade média do veículo durante a viagem?"))
distancia= (velocidade * t)
gasolina = (distancia/12)
print("A gasolina gasta foi:", round(gasolina, 4))