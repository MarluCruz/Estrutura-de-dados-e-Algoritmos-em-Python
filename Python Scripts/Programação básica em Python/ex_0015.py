#Respostas do exercício de expressões regulares.
import re
Numeros = "Meu novo númeor é (96) 98625-3576, mudei pois meu antigo número (34) 99975-2421 era foi vazado para grande Mídia. Cuidado pois eles acham que meu novo número é (48) 97436-4189"
print(re.findall('\(\d{2}\)\s\d{4,5}\-\d{4}', Numeros))
print(re.findall('\d', Numeros))
CEPs = "Olá senhor Tadeu o CEP que o senhor entregou no registro 63504-570 é do Ceará, contudo o senhor nunca morou lá. Eu posso registrar o CEP 94435-720? Atenciosamente Cláudia"
print(re.findall('\d{5}\-\d{3}', CEPs))
URLs = "Os sites que eu gasto mais tempo são https://www.youtube.com/, https://www.facebook.com/, mas o tempo que eu passo na https://www.udemy.com/ é um investimento para o meu futuro. Mas não resisto a lançamentos no mangahosted.com"
print(re.findall('https?://[A-za-z0-9./]+', URLs))