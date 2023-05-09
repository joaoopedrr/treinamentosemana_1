from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

print("Idade:", idade)

if idade < 18:
    tempo_falta = 18 - idade
    print("Faltam", tempo_falta, "ano(s) para o seu alistamento.")
elif idade == 18:
    print("É hora de se alistar!")
else:
    tempo_atraso = idade - 18
    print("Você já passou", tempo_atraso, "ano(s) do prazo de alistamento.")


