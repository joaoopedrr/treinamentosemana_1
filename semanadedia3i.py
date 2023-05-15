import random

jogadores = {}  


for i in range(1, 5):
    resultado = random.randint(1, 6)  
    jogadores[f"Jogador {i}"] = resultado

print("Resultados dos jogadores:")
for jogador, resultado in jogadores.items():
    print(f"{jogador}: {resultado}")


jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

print("\nClassificação final:")
for i, (jogador, resultado) in enumerate(jogadores_ordenados, start=1):
    print(f"Posição {i}: {jogador} - Resultado: {resultado}")
    
vencedor = jogadores_ordenados[0][0]
print(f"\nO vencedor é: {vencedor}")
