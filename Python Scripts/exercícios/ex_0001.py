# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
l1 = []
for i in range(1,6):
    n = int(input("Digite um número inteiro:"))
    l1.insert(i, n)
n = 0
soma = 0
for i in l1:
    soma += i

print(soma)