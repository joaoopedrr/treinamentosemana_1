soma_idades = 0
media_idade = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(1, 5):
    print(f"--- Pessoa {i} ---")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ")

    soma_idades += idade

    if sexo.upper() == "M":
        if idade > idade_homem_mais_velho:
            homem_mais_velho = nome
            idade_homem_mais_velho = idade
    elif sexo.upper() == "F":
        if idade < 20:
            mulheres_menos_20 += 1

media_idade = soma_idades / 4

print(f"A média de idade do grupo é {media_idade:.1f} anos.")
print(f"O homem mais velho é {homem_mais_velho}.")
print(f"{mulheres_menos_20} mulher(es) tem menos de 20 anos.")
