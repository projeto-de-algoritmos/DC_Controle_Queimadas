import pandas as pd
import os
import json
import numpy as np
import time
from funcoesMonitoramento import *

# df = pd.read_csv('forestFire.csv')
# df = df.drop_duplicates(subset=['Latitude', 'Longitude'], keep='first')
# df.to_json('forestFire.json', orient='records', lines=True)

DISTANCIA_SEGURANCA = 0.001

def main():
    with open('forestFire.json') as json_file:
        data = json.load(json_file)

    apresentaIntroducao()
    
    while True:
        os.system("clear")
        opcao = exibeMenu()
        if opcao == 1:
                focosIncendio = {}
                focosIncedio = converteDadosJsonParaDicionario(data, focosIncendio)
                propagacoes = 0
                while True:
                        p1, p2, dist = realizarMonitoramento(focosIncendio)
                        
                        if dist > DISTANCIA_SEGURANCA:
                                print("\n---------------------------------------------------")
                                print("|             \033[0;32mNão há mais focos próximos\033[0m           |")
                                print("---------------------------------------------------")
                                print("Total de propagações evitadas: ", propagacoes)
                                input("Aperte ENTER para sair")
                                break
                                
                        else:
                                os.system("clear")
                                print("Há focos de Incêndio muito próximos! " ,"\033[1;31m RISCO ALTO DE PROPAGAÇÃO\033[0m")
                                print("\nDistância de segurança: ", DISTANCIA_SEGURANCA)
                                print("Propagações evitadas: ", propagacoes)
                                print("\n\n============== DADOS DOS FOCOS =========================")
                                print("FOCO 1\n")
                                print("Número do foco: ", p1[0])
                                print("Nome do incidente: ", p1[1]['nome'])
                                print("Condado: ", p1[1]['condado'])
                                print("Latitude: ", p1[1]['y'])
                                print("Longitude: ", p1[1]['x'])
                                print("Causa: ", p1[1]['causa'])
                                print("Complexidade: ", p1[1]['complexidade'])
                                print("Tipo de propriedade: ", p1[1]['tipo de propriedade'])
                                print("\nFOCO 2\n")
                                print("Número do foco: ", p2[0])
                                print("Nome do incidente: ", p2[1]['nome'])
                                print("Condado: ", p2[1]['condado'])
                                print("Latitude: ", p2[1]['y'])
                                print("Longitude: ", p2[1]['x'])
                                print("Causa: ", p2[1]['causa'])
                                print("Complexidade: ", p2[1]['complexidade'])
                                print("Tipo de propriedade: ", p2[1]['tipo de propriedade'])
                                print("\n=============== Distância entre os focos =================")
                                print(dist)
                                print("\n\n\033[1;31mEnviando reforços...\033[0m")
                                del focosIncedio[p1[0]], focosIncedio[p2[0]]
                                time.sleep(1.5)
                                print("\033[1;34mSituação controlada!\033[0m")
                                time.sleep(0.5)
                                propagacoes+=1

        else:
            os.system("clear")
            print("Programa encerrado!")
            break
    
    


main()