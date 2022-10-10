boletim = {}
for _ in range(1,4):
    Aluno = str(input("Digite o nome do aluno:"))
    Nota = float(input("Digite a nota do Aluno:"))
    boletim[Aluno] = Nota
with open('text_0002.txt', 'w') as text:
  for aluno, nota in boletim.items():
    text.write(f'{aluno},{nota}\n')
