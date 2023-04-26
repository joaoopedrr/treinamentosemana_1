distancia=float(input("Qual a distancia em km:"))
print("Você fará uma viajem de {}".format(distancia))
if distancia<=200:
    preço=distancia*1.50
else:
    preço=distancia*1.25
print("O preço de sua passagem será de {}".format(preço))