with open('texts/text_0001.txt') as text:
    for linha in text:
        print(linha)
with open('texts/text_0001.txt') as text:
    r = text.readlines()
print(r)
with open('text_0002.txt', 'w') as texto:
    texto.write('Hoje foi um dia muito bom e produtivo. Estou muito feliz!')