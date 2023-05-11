import random

numeros_aleatorios = tuple(random.sample(range(1, 101), 5))

print("Listagem de números gerados:")
for numero in numeros_aleatorios:
    print(numero)

maior_valor = max(numeros_aleatorios)
menor_valor = min(numeros_aleatorios)

print(f"\nMaior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
