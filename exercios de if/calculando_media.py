n1 = float(input("digite a nota do aluno : "))
n2 = float(input("digite a nota do aluno : "))
n3 = float(input("digite a nota do aluno : "))
media = (n1 + n2 + n3) / 3

if media >= 7:
    print ("aprovado")
elif media >= 5 and media < 7:
    print ("aluno de recuperação ")
else:
    print ("aluno reprovado")