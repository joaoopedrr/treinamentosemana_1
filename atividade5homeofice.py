salario = float(input("Digite o valor do salário recebido: "))
despesas = float(input("Digite o total gasto em despesas: "))

if despesas <= salario:
    print("Gastos dentro do orçamento")
else:
    print("Gastos acima do orçamento")