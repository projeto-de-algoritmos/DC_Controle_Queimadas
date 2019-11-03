import pandas as pd
import os
import json
from funcoesMonitoramento import *

# df = pd.read_csv('forestFire.csv')
# df = df.drop_duplicates(subset=['Latitude', 'Longitude'], keep='first')
# df.to_json('forestFire.json', orient='records', lines=True)

DISTANCIA_SEGURANCA = 0.001

def main():
    with open('forestFire.json') as json_file:
        data = json.load(json_file)

    focosIncendio = {}
    focosIncedio = converteDadosJsonParaDicionario(data, focosIncendio)
    apresentaIntroducao()
    
    while True:
        os.system("clear")
        opcao = exibeMenu()
        if opcao == 1:

            while True:
                p1, p2, dist = realizarMonitoramento(focosIncendio)
                print(p1)
                print(p2)
                print(dist)
                if dist > DISTANCIA_SEGURANCA:
                    print("Não há mais focos próximos")
                    input()
                    break
                    
                else:
                    print("Focos de Incêndio muito próximos! RISCO ALTO DE PROPAGAÇÃO")
                    print("Enviando reforços...")
                    del focosIncedio[p1[0]], focosIncedio[p2[0]]
                    input()

        else:
            os.system("clear")
            print("Programa encerrado!")
            break


main()