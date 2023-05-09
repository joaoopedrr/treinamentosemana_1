valor_casa = float(input("Digite o valor da casa: R$ "))
salario_comprador = float(input("Digite o salário do comprador: R$ "))
anos_pagamento = int(input("Digite o número de anos para pagamento: "))

valor_prestacao = valor_casa / (anos_pagamento * 12) 

if valor_prestacao <= (salario_comprador * 0.3):  
    print("Empréstimo aprovado! O valor da prestação mensal é de R$ {:.2f}".format(valor_prestacao))
else:
    print("Empréstimo negado. O valor da prestação mensal excede 30% do salário.")