def encontrar_vogais(palavra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogais_encontradas = []

    for letra in palavra:
        if letra.lower() in vogais:
            vogais_encontradas.append(letra)

    return vogais_encontradas

palavras = ('python', 'programacao', 'openai', 'linguagem', 'modelo')

for palavra in palavras:
    print(f'Vogais em "{palavra}": {encontrar_vogais(palavra)}')
