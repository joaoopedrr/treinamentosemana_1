def escreva(texto):
    linha = '-' * (len(texto) + 4)
    print(linha)
    print(f"| {texto} |")
    print(linha)


escreva("Olá, Mundo!")
