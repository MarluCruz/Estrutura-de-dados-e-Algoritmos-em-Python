#Espressões regulares com Espressões regulares com a função match
import re
frase = 'A placa de carro que eu anotei durante a batida foi FRT-1998'
print(re.match('[A-Za-z]{3}-\d{4}', frase))
frase2 = 'FRT-1998 é a placa do carro'
print(re.match('[A-Za-z]{3}-\d{4}', frase2))
