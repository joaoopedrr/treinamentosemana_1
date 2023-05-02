frase = input("Digite uma frase: ")


frase_sem_espacos = frase.replace(" ", "")


numero_caracteres = len(frase_sem_espacos)


print(f"A frase digitada foi: {frase}")
print(f"A quantidade de caracteres (sem contar espaços) é: {numero_caracteres}")