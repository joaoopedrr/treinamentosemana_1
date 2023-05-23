def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

n = leiaInt('Digite um número inteiro: ')
print("Número digitado:", n)
