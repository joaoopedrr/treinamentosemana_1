import random

jogadores = ['Jogador 1', 'Jogador 2', 'Jogador 3', 'Jogador 4']
resultados = {}

for jogador in jogadores:
    resultado = random.randint(1, 6)
    resultados[jogador] = resultado

print("Resultados dos jogadores:")
for jogador, resultado in resultados.items():
    print(jogador, "tirou", resultado)

resultados_ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)

print("\nClassificação final:")
for i, (jogador, resultado) in enumerate(resultados_ordenados):
    print(f"{i+1}º lugar: {jogador} - {resultado} pontos")
