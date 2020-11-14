#coding: utf-8

from random import randint
from estacao import Estacao
from utils import verificaColisao

def csmaPPersistente(estacoes, n):
    slotAtual = transmissoes = flagPrimeira = 0
    estacoesCandidatas = []
    estacoesParaTransmitir = []
    p = 0.01

    while transmissoes < n:
        if slotAtual == 0:
            slotAtual = 1
        else:
            for e in estacoes:#Verifica se há estações para serem transmitidas no slot atual
                if e.getSlot() == slotAtual:
                    estacoesCandidatas.append(e)
            
            for eC in estacoesCandidatas:#Verifica a probabilidade de cada estação candidata a transmitir
                probabilidade = randint(0, 2)
                if probabilidade <= p:#Caso a estação tenha probabilidade de transmitir
                    estacoesParaTransmitir.append(eC)
                else:
                    for e in estacoes:#Caso não tenha a estação tentará novamente no próximo slot
                        if e.getIdEstacao() == eC.getIdEstacao():
                            e.setSlot(slotAtual+1)
                            break
            estacoesCandidatas.clear()
            
            
            flagColisao = verificaColisao(estacoesParaTransmitir)#Verifica a ocorrência de colisão
            if flagColisao == 0:
                for e in estacoes:#Realiza a transmissão do quadro da estação
                    if e.getIdEstacao() == estacoesParaTransmitir[0].getIdEstacao():
                        e.setTransmitiu()
                        break
                transmissoes += 1
                if flagPrimeira == 0:
                    slotPrimeira = estacoesParaTransmitir[0].getSlot()
                    flagPrimeira = 1
            elif flagColisao == 1:
                for e in estacoes:#Trata a colisão gerando o próximo slot para as estações que colidiram
                    for eT in estacoesParaTransmitir:
                        if e.getIdEstacao() == eT.getIdEstacao():
                            e.setSlot(randint(slotAtual+1, slotAtual+n))
            slotAtual += 1
            estacoesParaTransmitir.clear()
    
    #Retorna o total de slots de tempo gastos e o tempo gasto da primeira estação
    return slotPrimeira, slotAtual
            
            

