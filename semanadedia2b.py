import random

def get_jogada_computador():
    jogadas = ["Pedra", "Papel", "Tesoura"]
    return random.choice(jogadas)

def determinar_vencedor(jogada_usuario, jogada_computador):
    if jogada_usuario == jogada_computador:
        return "Empate"
    elif (
        (jogada_usuario == "Pedra" and jogada_computador == "Tesoura") or
        (jogada_usuario == "Papel" and jogada_computador == "Pedra") or
        (jogada_usuario == "Tesoura" and jogada_computador == "Papel")
    ):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
print("Escolha sua jogada:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

opcoes = ["Pedra", "Papel", "Tesoura"]
escolha_usuario = int(input("Digite o número correspondente à sua jogada: ")) - 1

if escolha_usuario >= 0 and escolha_usuario <= 2:
    jogada_usuario = opcoes[escolha_usuario]
    jogada_computador = get_jogada_computador()

    print("Você jogou:", jogada_usuario)
    print("O computador jogou:", jogada_computador)

    resultado = determinar_vencedor(jogada_usuario, jogada_computador)
    print(resultado)
else:
    print("Opção inválida. Por favor, escolha um número de 1 a 3 para jogar.")
