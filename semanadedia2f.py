sexo = input("Digite o sexo (M/F): ")

while sexo.upper() != "M" and sexo.upper() != "F":
    print("Valor incorreto. Digite 'M' para masculino ou 'F' para feminino.")
    sexo = input("Digite o sexo (M/F): ")

print("Sexo registrado:", sexo.upper())