import datetime

pessoa = {}

pessoa['nome'] = input("Digite o nome da pessoa: ")
ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
pessoa['idade'] = datetime.date.today().year - ano_nascimento
pessoa['ctps'] = int(input("Digite o número da carteira de trabalho (0 se não tiver): "))

if pessoa['ctps'] != 0:
    pessoa['ano_contratacao'] = int(input("Digite o ano de contratação: "))
    pessoa['salario'] = float(input("Digite o salário: "))
    pessoa['idade_aposentadoria'] = pessoa['idade'] + (65 - (datetime.date.today().year - pessoa['ano_contratacao']))
else:
    pessoa['idade_aposentadoria'] = 'N/A'

print("\nDados da pessoa:")
for chave, valor in pessoa.items():
    print(chave.capitalize() + ":", valor)
