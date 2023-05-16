
numeros = []

while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    
    
    if numero == 0:
        break
    
    numeros.append(numero)


quantidade = len(numeros)


numeros.sort(reverse=True)


valor_5 = 5 in numeros


print(f"Quantidade de números digitados: {quantidade}")
print(f"Lista de valores em ordem decrescente: {numeros}")
print(f"O valor 5 {'está' if valor_5 else 'não está'} na lista.")
