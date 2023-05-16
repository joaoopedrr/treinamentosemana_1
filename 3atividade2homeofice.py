produtos = (
    ("Arroz", 10.99),
    ("Feijão", 5.99),
    ("Macarrão", 3.49),
    ("Leite", 2.99),
    ("Café", 7.99)
)

print("LISTAGEM DE PREÇOS")
print("-" * 30)
print("PRODUTO\t\tPREÇO")
print("-" * 30)
for produto, preco in produtos:
    print(f"{produto: <10}\tR${preco:.2f}")
print("-" * 30)
