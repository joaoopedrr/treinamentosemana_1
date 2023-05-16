jogador = {}

jogador["nome"] = input("Digite o nome do jogador: ")
quantidade_partidas = int(input("Digite a quantidade de partidas jogadas: "))

gols_total = 0
gols_partidas = []

for partida in range(quantidade_partidas):
    gols_partida = int(input(f"Digite a quantidade de gols feitos na partida {partida + 1}: "))
    gols_total += gols_partida
    gols_partidas.append(gols_partida)

jogador["gols_total"] = gols_total
jogador["gols_partidas"] = gols_partidas

print("\nDADOS DO JOGADOR:")
print("Nome:", jogador["nome"])
print("Total de gols no campeonato:", jogador["gols_total"])
print("Gols em cada partida:", jogador["gols_partidas"])
