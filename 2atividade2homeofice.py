nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("Média:", media)

if media < 5.0:
    print("REPROVADO")
elif media >= 5.0 and media < 7.0:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")