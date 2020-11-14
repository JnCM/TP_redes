#coding: utf-8

from statistics import mean, pstdev
from estacao import Estacao

#Inicializa a lista de estações
def inicializa(n):
    estacoes = []
    for i in range(n):
        estacoes.append(Estacao(i+1))
    
    return estacoes

#Verifica a ocorrência de colisões
def verificaColisao(estacoes):
    qtdeEstacoes = len(estacoes)
    if qtdeEstacoes > 1:
        return 1#Caso houver colisão em um dado slot
    elif qtdeEstacoes == 0:
        return -1#Caso não houver estações num dado slot
    return 0#Caso não houver colisões

#Realiza o cálculo da média e do desvio padrão de uma simulação
def calculaResultado(slots, slotsPrimeira):
    tempoCanal = 51.2#Duração de um canal de tempo: 51.2 us

    for i in range(len(slotsPrimeira)):
        slotsPrimeira[i] = slotsPrimeira[i]*tempoCanal

    mediaPrimeira = mean(slotsPrimeira)
    desvioPadraoPrimeira = pstdev(slotsPrimeira)
    
    print("-------------------------- Primeira estação ---------------------------------")
    print(" Média = {} us".format(round(mediaPrimeira, ndigits=3)))
    print(" Desvio padrão = {} us".format(round(desvioPadraoPrimeira, ndigits=3)))
    print("-----------------------------------------------------------------------------")
    
    for i in range(len(slots)):
        slots[i] = slots[i]*tempoCanal
    
    media = mean(slots)#Retorna a média
    desvioPadrao = pstdev(slots)#Retorna o desvio padrão

    print("-------------------------- Resultado Total ----------------------------------")
    print(" Média = {} us".format(round(media, ndigits=3)))
    print(" Desvio padrão = {} us".format(round(desvioPadrao, ndigits=3)))
    print("-----------------------------------------------------------------------------")