def inserir_ordenado(lista, valor):
    if len(lista) == 0:
        lista.append(valor)
    else:
        for i in range(len(lista)):
            if valor < lista[i]:
                lista.insert(i, valor)
                break
        else:
            lista.append(valor)

numeros = []

for _ in range(5):
    valor = float(input("Digite um valor numérico: "))
    inserir_ordenado(numeros, valor)

print("Lista ordenada:")
print(numeros)








