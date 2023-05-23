def contador(inicio, fim, passo):
    if passo == 0:
        print("O valor do passo não pode ser zero.")
        return

    if passo > 0:
        if inicio > fim:
            passo *= -1
        fim += 1
    else:
        if inicio < fim:
            passo *= -1
        fim -= 1

    for i in range(inicio, fim, passo):
        print(i, end=" ")
    print()

contador(1, 10, 1)

contador(10, 0, -2)

inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
passo = int(input("Digite o valor do passo: "))
contador(inicio, fim, passo)
