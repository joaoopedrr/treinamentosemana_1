def ficha(nome="Desconhecido", gols=0):
    print("Ficha do jogador:")
    print("Nome:", nome)
    print("Gols marcados:", gols)

nome_jogador = input("Digite o nome do jogador: ")
gols_jogador = input("Digite a quantidade de gols marcados pelo jogador: ")

if gols_jogador.isdigit():
    gols_jogador = int(gols_jogador)
    ficha(nome_jogador, gols_jogador)
else:
    ficha(nome_jogador)
