import time

def contagem_regressiva(tempo):
    while tempo > 0:
        print(tempo)
        time.sleep(1)
        tempo -= 1
    print("Estouro de fogos de artifício!")

contagem_regressiva(10)