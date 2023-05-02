ano_nascimento = int(input("Digite o ano de nascimento: "))


idade = 2023 - ano_nascimento

if idade >= 18:
    print(f"Você tem {idade} anos e é maior de idade.")
else:
    print(f"Você tem {idade} anos e é menor de idade.")