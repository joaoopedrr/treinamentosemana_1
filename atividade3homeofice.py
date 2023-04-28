valor = float(input("Digite um valor: ")) # pede um valor ao usuário e converte para float

if valor > 0: # verifica se o valor é maior que zero
    print("O valor é positivo!")
elif valor < 0: # verifica se o valor é menor que zero
    print("O valor é negativo!")
else: # caso contrário, o valor é igual a zero
    print("O valor é igual a zero!")