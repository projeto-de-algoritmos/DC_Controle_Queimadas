import time
import numpy as np
import math


def apresentaIntroducao():
    print("Bem vindo ao sistema de monitoramento de incêndios de Nova Iorque!")
    time.sleep(1)

def exibeMenu():
    print("============= Menu Principal ====================")
    print("1 - Monitorar focos de incêndio")
    print("0 - Sair")
    opcao = recebeOpcao("O que você deseja ? ", 0, 1)
    return opcao

def recebeOpcao(mensagem, min, max):
    opcao = int(input(mensagem))
    while(opcao < int(min) or opcao > int(max)):
        print("Opção inválida! Por favor, digite novamente!")
        opcao = int(input(mensagem))

    return opcao

def converteDadosJsonParaDicionario(json_object, focosIncendio):
    for foco in json_object:
        focosIncendio[foco['Fire Number']] = {}
        focosIncendio[foco['Fire Number']]['x'] = foco['Longitude']
        focosIncendio[foco['Fire Number']]['y'] = foco['Latitude']
        focosIncendio[foco['Fire Number']]['nome'] = foco['Incident Name']
        focosIncendio[foco['Fire Number']]['condado'] = foco['County']
        focosIncendio[foco['Fire Number']]['causa'] = foco['Cause']
        focosIncendio[foco['Fire Number']]['complexidade'] = foco['Complex Type']
        focosIncendio[foco['Fire Number']]['tipo de propriedade'] = foco['Ownership']
    return focosIncendio

def montaDicionarioPontosPosicoes(json_object, posicoes):
    for foco in json_object:
        posicoes[foco['Fire Number']] = []
        posicoes[foco['Fire Number']].append(foco['Longitude'])
        posicoes[foco['Fire Number']].append(foco['Latitude'])
    return posicoes

def realizarMonitoramento(focosIncendio):
    focosIncendioOrdenadoPorX = sorted(focosIncendio.items(), key=lambda x: x[1]['x'])
    focosIncendioOrdenadoPorY = sorted(focosIncendio.items(), key=lambda x: x[1]['y'])
    ponto1, ponto2, distanciaEntrePontos = calculaParPontosMaisProximos(focosIncendioOrdenadoPorX, focosIncendioOrdenadoPorY)
    return ponto1, ponto2, distanciaEntrePontos

def calculaDistanciaEuclidianaEntrePontos(p1, p2):
    distanciaEuclidiana = np.sqrt((p1[1]['x'] - p2[1]['x'])**2 + (p1[1]['y']-p2[1]['y'])**2)

    return distanciaEuclidiana

def calculaParPontosMaisProximos(focosIncendioOrdenadoPorX, focosIncendioOrdenadoPorY):
    tamanhofocosIncendioOrdenadoPorX = len(focosIncendioOrdenadoPorX)
    if tamanhofocosIncendioOrdenadoPorX <= 3:
        return calculaParPontosMaisProximosForcaBruta(focosIncendioOrdenadoPorX)
    meio = tamanhofocosIncendioOrdenadoPorX // 2
    
    esquerdaX = focosIncendioOrdenadoPorX[:meio]
    direitaX = focosIncendioOrdenadoPorX[meio:]
    
    pontoMeio = focosIncendioOrdenadoPorX[meio][1]['x']
    
    esquerdaY = list()
    direitaY = list()

    for ponto in focosIncendioOrdenadoPorY:
        if ponto[1]['x'] <= pontoMeio:
            esquerdaY.append(ponto)
        else:
            direitaY.append(ponto)
  
    (p1, q1, distancia1) = calculaParPontosMaisProximos(esquerdaX, esquerdaY)
    (p2, q2, distancia2) = calculaParPontosMaisProximos(direitaX, direitaY)

    if distancia1 <= distancia2:
        distanciaLados = distancia1
        minimo = (p1, q1)
    else:
        distanciaLados = distancia2
        minimo = (p2, q2)
    
    (p3, q3, distancia3) = calculaParPontosDivisao(focosIncendioOrdenadoPorX, focosIncendioOrdenadoPorY, distanciaLados, minimo)

    if distanciaLados <= distancia3:
        return minimo[0], minimo[1], distanciaLados
    else:
        return p3, q3, distancia3

def calculaParPontosMaisProximosForcaBruta(focosIncendioOrdenadoPorX):
    distanciaPrimeiros = calculaDistanciaEuclidianaEntrePontos(focosIncendioOrdenadoPorX[0], focosIncendioOrdenadoPorX[1])
    p1 = focosIncendioOrdenadoPorX[0]
    p2 = focosIncendioOrdenadoPorX[1]
    tamanhofocosIncendioOrdenadoPorX = len(focosIncendioOrdenadoPorX)
    
    if tamanhofocosIncendioOrdenadoPorX == 2:
        return p1, p2, distanciaPrimeiros
    
    for i in range(tamanhofocosIncendioOrdenadoPorX-1):
        for j in range(i+1, tamanhofocosIncendioOrdenadoPorX):
            if i != 0 and j != 1:
                distancia = calculaDistanciaEuclidianaEntrePontos(focosIncendioOrdenadoPorX[i], focosIncendioOrdenadoPorX[j])
                if distancia < distanciaPrimeiros:
                    distanciaPrimeiros = distancia
                    p1, p2 = focosIncendioOrdenadoPorX[i], focosIncendioOrdenadoPorX[j]
    
    return p1, p2, distanciaPrimeiros

def calculaParPontosDivisao(focosIncendioOrdenadoPorX, focosIncendioOrdenadoPorY, distanciaLados, minimo):
    tamanhofocosIncendioOrdenadoPorX = len(focosIncendioOrdenadoPorX)
    meio = tamanhofocosIncendioOrdenadoPorX // 2
    xPontoDivisao = focosIncendioOrdenadoPorX[meio][1]['x']

    subarray_y = [ponto for ponto in focosIncendioOrdenadoPorY if xPontoDivisao - distanciaLados <= ponto[1]['x'] <= xPontoDivisao + distanciaLados]
    menorDistancia = distanciaLados
    tamanhofocosIncendioOrdenadoPorY = len(subarray_y)

    for i in range(tamanhofocosIncendioOrdenadoPorY - 1):
        for j in range(i+1, min(i+7, tamanhofocosIncendioOrdenadoPorY)):
            p, q = subarray_y[i], subarray_y[j]
            distancia = calculaDistanciaEuclidianaEntrePontos(p, q)
            if distancia < menorDistancia:
                minimo = p, q
                menorDistancia = distancia
    return minimo[0], minimo[1], menorDistancia