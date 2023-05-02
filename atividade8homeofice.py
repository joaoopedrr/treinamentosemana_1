string = "treinamento de back-end"


palavra_antiga = input("Digite a palavra a ser substituída: ")
nova_palavra = input("Digite a nova palavra: ")


nova_string = string.replace(palavra_antiga, nova_palavra)


print("Nova string: ", nova_string)