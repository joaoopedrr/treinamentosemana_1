import random

vitorias_consecutivas = 0

while True:
    jogador = int(input("Escolha um número (0 a 10): "))
    escolha = input("Par ou Ímpar? (P/I): ").upper()
    
    while escolha != 'P' and escolha != 'I':
        escolha = input("Escolha inválida. Par ou Ímpar? (P/I): ").upper()
    
    computador = random.randint(0, 10)
    
    print("Jogador:", jogador)
    print("Computador:", computador)
    
    soma = jogador + computador
    
    print("Soma:", soma)
    
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    
    if resultado == escolha:
        print("Você venceu!")
        vitorias_consecutivas += 1
    else:
        print("Você perdeu!")
        break

print("Total de vitórias consecutivas:", vitorias_consecutivas)