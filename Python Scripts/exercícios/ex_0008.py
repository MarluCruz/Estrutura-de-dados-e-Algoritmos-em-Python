lista = []
try:
    while True:
        try: 
            while 2 > len(lista):       
                Numero = float(input("Digite um número:"))
                lista.append(Numero)
        except ValueError:
            print("Valor inválido, Por favor digite um número!")
        except IndexError:
            print("Por favor digite um valor válido!")
        else:
        #print("Os valores digitados foram", lista)
            break    
    while True:
        try:
            divisão = lista [0] / lista [1]
        except ZeroDivisionError:
            print("Impossível dividir por zero!")
            Numero = float(input("Digite um número:"))
            lista.insert(1, Numero)
        else:
            print("A divisão de um pelo outro é igual a:", divisão)
            break
except KeyboardInterrupt:
            print("A execução foi interrompida!")