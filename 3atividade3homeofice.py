
valores = []

while True:
    valor = int(input("Digite um valor (ou 0 para sair): "))
 
    if valor == 0:
        break
    elif valor in valores:
        print("Valor já existe na lista. Não será adicionado.")
    else:
        valores.append(valor)


valores.sort()


print("Valores únicos em ordem crescente:")
for valor in valores:
    print(valor)
