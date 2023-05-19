def maior(*valores):
    if len(valores) == 0:
        return None
    
    maior_valor = valores[0]
    
    for valor in valores:
        if valor > maior_valor:
            maior_valor = valor
    
    return maior_valor


resultado = maior(5, 10, 3, 8, 1)
print("O maior valor é:", resultado)
