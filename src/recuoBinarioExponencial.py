#coding: utf-8

from random import randint
from estacao import Estacao
from utils import verificaColisao

#Método que simula a execução do algoritmo Recuo binário exponencial
def backOffExponencial(estacoes, n):
    slotAtual = transmissoes = flagPrimeira = 0
    estacoesParaTransmitir = []

    while transmissoes < n:
        if slotAtual == 0:
            slotAtual = 1
        else:
            for e in estacoes:#Verifica se há estações para serem transmitidas no slot atual
                if e.getSlot() == slotAtual:
                    estacoesParaTransmitir.append(e)
            
            flagColisao = verificaColisao(estacoesParaTransmitir)#Verifica a ocorrência de colisão
            if flagColisao == 0:
                for e in estacoes:#Realiza a transmissão do quadro da estação
                    if e.getIdEstacao() == estacoesParaTransmitir[0].getIdEstacao():
                        e.setTransmitiu()
                        break
                transmissoes += 1
                if flagPrimeira == 0:#Resgata o tempo gasto da primeira estação
                    slotPrimeira = estacoesParaTransmitir[0].getSlot()
                    flagPrimeira = 1
            elif flagColisao == 1:#Trata a colisão gerando o próximo slot para as estações que colidiram
                for e in estacoes:
                    for eT in estacoesParaTransmitir:
                        if e.getIdEstacao() == eT.getIdEstacao():
                            e.incrementaColisao()#Atualiza o número de colisões de uma estação
                            if e.getNColisoes() == 16:#Caso o número de colisões chegue no limite de tentativas
                                n -= 1#A estação desiste de transmitir
                            elif e.getNColisoes() > 10:#Caso a estação chegue à mais de 10 colisões
                                espera = randint(0, int(pow(2, 10))-1)#O limite superior do rand é fixado
                                e.setSlot(slotAtual+1+espera)
                            else:#Senão a estação continua tendo o range de espera incremental
                                espera = randint(0, int(pow(2, e.getNColisoes()))-1)
                                e.setSlot(slotAtual+1+espera)
            
            slotAtual += 1
            estacoesParaTransmitir.clear()

    #Retorna o total de slots de tempo gastos e o tempo gasto da primeira estação
    return slotPrimeira, slotAtual, n