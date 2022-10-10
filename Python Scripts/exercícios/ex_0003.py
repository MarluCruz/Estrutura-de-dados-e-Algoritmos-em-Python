# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 10:54:42 2022

@author: Admin
"""

alunos = {}
for _ in range(1, 4):
  nome = input('Digite o nome: ')
  nota = float(input('Digite a nota: '))
  alunos[nome] = nota 
soma = 0
i = 0
for nota in alunos.values():
    soma += nota
media = soma/3
print("A média dos alunos é:", media)