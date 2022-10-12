#Espressões regulares com a Função search
import re
frase = 'Olá, meu número de telefone é (42)00010-0000'
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', frase))
frase = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'
print(re.search('[A-Za-z]{3}-\d{4}', frase))
email = 'Entre em contato, meu email é teste@teste.com'
print(re.search('\w+@\w+\.com', email))