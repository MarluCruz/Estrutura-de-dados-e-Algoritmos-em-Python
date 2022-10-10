# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

idade = int(input("Digite a sua idade, no caso de bebês com menos de 1 ano digite 0:"))
if (idade >= 0) and (idade <= 12):
    print("Criança")
else:
    if (idade >= 13) and (idade <= 17):
        print("Adolescente")
    else:
        if (idade >=18):
            print("Adulto")
        else:
            print("Idade inválida:")