import random

quantidade_jogos = int(input("Quantos jogos você deseja gerar? "))

jogos = []

for _ in range(quantidade_jogos):
    jogo = random.sample(range(1, 51), 5)
    jogos.append(jogo)

print("Palpites gerados:")
for i, jogo in enumerate(jogos, 1):
    print(f"Jogo {i}: {jogo}")