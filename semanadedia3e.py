
numeros = []


pares = []
impares = []

while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))
    
    if numero == 0:
        break
    
    numeros.append(numero)
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números digitados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
