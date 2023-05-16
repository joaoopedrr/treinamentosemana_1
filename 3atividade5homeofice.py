numeros = []
pares = []
impares = []

while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")
    
    if numero.lower() == "sair":
        break
    
    numero = int(numero)
    numeros.append(numero)
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números digitados:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)
