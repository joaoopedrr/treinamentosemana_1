maior_peso = float('-inf')  
menor_peso = float('inf')  

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print(f"O maior peso lido foi {maior_peso} kg.")
print(f"O menor peso lido foi {menor_peso} kg.")