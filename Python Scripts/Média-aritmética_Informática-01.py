# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 20:35:35 2022

@author: Admin
"""

M1 = float(input("Digite a sua nota da M1:"))
M2 = float(input("Digite sua nota da M2:"))
M3 = float(input("Digite sua nota da M3:"))
Media = ((M1+M2+M3)/3)
if (Media >= 0) and (Media <=4.0):
    print("O aluno está reprovado!")
else:
    if (Media >= 4.1) and (Media <=6.0):
        print("O aluno pegou exame!")
        Nota_Exame = float(input("Digite a nota do exame:"))
        if (Nota_Exame >= 6.1):
            print("Aluno Aprovado!")
        else:
            print("Aluno Reprovado!")
    else:
        if (Media >= 6.1):
            print("O Aluno foi aprovado:")