
numeros = []

for _ in range(5):
    valor = int(input("Digite um valor numérico: "))
    numeros.append(valor)


pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]


pares.sort()
impares.sort()

print("Valores pares:", pares)
print("Valores ímpares:", impares)
