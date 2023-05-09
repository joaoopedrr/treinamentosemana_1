def soma(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def maior(a, b):
    if a > b:
        return a
    else:
        return b

def exibir_menu():
    print("[1] SOMA")
    print("[2] MULTIPLICAR")
    print("[3] MAIOR")
    print("[4] NOVOS NÚMEROS")
    print("[5] SAIR DO PROGRAMA")

exibir_menu()

opcao = int(input("Digite a opção desejada: "))
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

while opcao != 5:
    if opcao == 1:
        resultado = soma(numero1, numero2)
        print("Resultado da soma:", resultado)
    elif opcao == 2:
        resultado = multiplicar(numero1, numero2)
        print("Resultado da multiplicação:", resultado)
    elif opcao == 3:
        resultado = maior(numero1, numero2)
        print("Maior número:", resultado)
    elif opcao == 4:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    else:
        print("Opção inválida.")

    exibir_menu()
    opcao = int(input("Digite a opção desejada: "))

print("Programa encerrado.")
