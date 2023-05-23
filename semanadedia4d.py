def voto(ano_nascimento):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return "NEGADO"
    elif 16 <= idade < 18 or idade >= 70:
        return "OPCIONAL"
    else:
        return "OBRIGATÓRIO"

ano = int(input("Digite o ano de nascimento: "))
resultado = voto(ano)
print("Voto:", resultado)