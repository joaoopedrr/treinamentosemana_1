alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    
    if nome.lower() == "sair":
        break
    
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    
    aluno = [nome, nota1, nota2]
    alunos.append(aluno)

print("Boletim:")
for aluno in alunos:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    media = (nota1 + nota2) / 2
    
    print("Aluno:", nome)
    print("Média:", media)
    print()

while True:
    opcao = input("Digite o nome do aluno para ver suas notas (ou 'sair' para encerrar): ")
    
    if opcao.lower() == "sair":
        break
    
    encontrado = False
    
    for aluno in alunos:
        nome = aluno[0]
        nota1 = aluno[1]
        nota2 = aluno[2]
        
        if nome.lower() == opcao.lower():
            encontrado = True
            print("Notas de", nome)
            print("Nota 1:", nota1)
            print("Nota 2:", nota2)
            print("Média:", (nota1 + nota2) / 2)
            print()
    
    if not encontrado:
        print("Aluno não encontrado.")
