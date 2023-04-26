import random
n1=(input("Primeiro aluno:"))
n2=(input("Segundo aluno:"))
n3=(input("Terceiro aluno:"))
lista= [n1, n2, n3]
sorteado= random.choice(lista)
print("O aluno sorteado foi {}".format(sorteado))