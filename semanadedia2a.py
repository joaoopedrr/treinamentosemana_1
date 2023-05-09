preco_produto = float(input("Digite o preço do produto: R$ "))
condicao_pagamento = input("Digite a condição de pagamento (dinheiro, pix, cartao): ")

if condicao_pagamento == "dinheiro" or condicao_pagamento == "pix":
    valor_pago = preco_produto * 0.9  
elif condicao_pagamento == "cartao":
    parcelas = int(input("Digite o número de parcelas (1 para à vista, 2 para 2x no cartão, 3 ou mais para 3x ou mais no cartão): "))
    if parcelas == 1:
        valor_pago = preco_produto * 0.95  
    elif parcelas == 2:
        valor_pago = preco_produto  
    elif parcelas >= 3:
        valor_pago = preco_produto * 1.2  
        print("Serão acrescentados 20% de juros no valor final.")
else:
    print("Condição de pagamento inválida.")

if valor_pago:
    print("O valor a ser pago é de R$ {:.2f}".format(valor_pago))