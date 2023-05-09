frase = input("Digite uma frase: ")


frase_sem_espacos = frase.replace(" ", "")


if frase_sem_espacos.lower() == frase_sem_espacos.lower()[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")