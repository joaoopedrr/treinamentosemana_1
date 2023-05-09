import random

numero_pensado = random.randint(0, 10)
tentativas = 0

print("Bem-vindo! Tente adivinhar o número que estou pensando.")

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    
    if palpite == numero_pensado:
        print("Parabéns! Você acertou o número em", tentativas, "tentativas.")
        break
    elif palpite < numero_pensado:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")