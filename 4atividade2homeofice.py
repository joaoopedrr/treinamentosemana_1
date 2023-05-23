import random

def sorteia():
    numeros = []
    for _ in range(5):
        numeros.append(random.randint(1, 10))
    return numeros

def somaPar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    return soma

numeros_sorteados = sorteia()

print("Números sorteados:", numeros_sorteados)

soma_pares = somaPar(numeros_sorteados)

print("Soma dos valores pares:", soma_pares)
