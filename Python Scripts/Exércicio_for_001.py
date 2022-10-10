# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:08:42 2022

@author: Admin
"""
i = 1
soma = 0
while i < 6:
    nota = float(print("Digite a nota:"))
    soma += nota
    i += 1
Media = soma/(i-1)
print("Sua média final foi:", Media)
