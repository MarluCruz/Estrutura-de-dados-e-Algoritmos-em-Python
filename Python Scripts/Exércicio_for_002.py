# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:29:09 2022

@author: Admin
"""
soma = 0
nota = 0
for nota in range(1,6):
    nota = float(input("Digite a sua nota:"))
    soma += nota
media = (soma/5)
print("Sua nota foi igual a:", media)