def exponenciacao (base, expoente):
    if expoente == 0:

        return 1
    else:
        return base * exponenciacao(base, expoente -1)

print(exponenciacao(4, 3))