valores = []

for i in range(5):
    valor = float(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

maior_valor = max(valores)
menor_valor = min(valores)

posicao_maior = valores.index(maior_valor)
posicao_menor = valores.index(menor_valor)

print(f"Valores digitados: {valores}")
print(f"Maior valor: {maior_valor} (posição: {posicao_maior})")
print(f"Menor valor: {menor_valor} (posição: {posicao_menor})")