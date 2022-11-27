#Recursão
def recurssao (i):
    print('Recursao')
    i+= 1
    if i == 5:
        return
    else:
        recurssao(i)
recurssao(0)