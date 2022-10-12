#Meu primeiro objeto e exercício de teoria básica de programação orientada aos objetos
class aluno:
    def __init__(self, nome, nota1, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota3
        self.Media = 0.0
    def media(self):
       self.Media = (self.nota1+self.nota2) /2
       return self.Media
    def dados(self):
        print("Nome:", self.nome)
        print("Nota1:", self.nota1)
        print("Nota2:", self.nota2)
        print("Media:", self.Media)
    def avalicao(self):
        if self.Media >= 6:
            print("Aprovado")
        else:
            print("reprovado")
       
nome = str(input("Digite o nome do Aluno:"))
nota1 = float(input("Digite a primeira nota do Aluno:"))
nota2 = float(input("Digite a segunda nota do Aluno:"))
aluno1 = aluno(nome, nota1, nota2)
aluno1.media()
aluno1.dados()
aluno1.avalicao()



