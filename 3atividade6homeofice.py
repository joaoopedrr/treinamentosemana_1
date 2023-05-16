pessoas = []
mais_pesadas = []
mais_leves = []
peso_maximo = float('-inf')
peso_minimo = float('inf')

while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para encerrar): ")
    
    if nome.lower() == "sair":
        break
    
    peso = float(input("Digite o peso da pessoa: "))
    
    pessoa = {
        "nome": nome,
        "peso": peso
    }
    
    pessoas.append(pessoa)
    
    if peso > peso_maximo:
        peso_maximo = peso
        mais_pesadas = [pessoa]
    elif peso == peso_maximo:
        mais_pesadas.append(pessoa)
    
    if peso < peso_minimo:
        peso_minimo = peso
        mais_leves = [pessoa]
    elif peso == peso_minimo:
        mais_leves.append(pessoa)

quantidade_pessoas = len(pessoas)

print("Quantidade de pessoas cadastradas:", quantidade_pessoas)

print("Pessoas mais pesadas:")
for pessoa in mais_pesadas:
    print("Nome:", pessoa["nome"])
    print("Peso:", pessoa["peso"])

print("Pessoas mais leves:")
for pessoa in mais_leves:
    print("Nome:", pessoa["nome"])
    print("Peso:", pessoa["peso"])
