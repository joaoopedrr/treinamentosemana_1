num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

if num1 == num2 and num2 == num3:
    print("Três iguais")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Dois iguais")
else:
    print("Três diferentes")