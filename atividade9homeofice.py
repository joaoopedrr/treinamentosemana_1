
string = input("Digite uma string: ")


contador = 0


for caractere in string:
    
    if caractere.isalpha():
        
        contador += 1


print("Número de letras na string: ", contador)