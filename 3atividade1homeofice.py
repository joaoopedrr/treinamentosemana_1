
valores = tuple(int(input(f"Digite o {i + 1}º valor: ")) for i in range(4))


contagem_9 = valores.count(9)


posicao_3 = valores.index(3) + 1 if 3 in valores else "não encontrado"


numeros_pares = [valor for valor in valores if valor % 2 == 0]


print(f"Quantidade de vezes que o valor 9 apareceu: {contagem_9}")
print(f"Posição do primeiro valor 3: {posicao_3}")
print(f"Números pares: {numeros_pares}")