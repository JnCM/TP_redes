#coding: utf-8

from random import randint
from estacao import Estacao
from utils import verificaColisao

#Método que simula a execução do algoritmo Slotted Aloha
def backOffExponencial(estacoes, n):
    slotAtual = transmissoes = flagPrimeira = 0
    tentativas = nColisoes = erro = 0
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
            elif flagColisao == 1:
                if tentativas == 6:#Caso chegue no limite de tentativas é retornado erro
                    erro = 1
                    break
                else:
                    if nColisoes < 10:#Incrementa o expoente até 10
                        nColisoes += 1
                    else:
                        tentativas += 1
                for e in estacoes:#Trata a colisão gerando o próximo slot para as estações que colidiram
                    for eT in estacoesParaTransmitir:
                        if e.getIdEstacao() == eT.getIdEstacao():
                            e.setSlot(randint(slotAtual+1, slotAtual+int(pow(2, nColisoes))+1))
            slotAtual += 1
            estacoesParaTransmitir.clear()

    if erro == 1:
        return 0, 0

    #Retorna o total de slots de tempo gastos e o tempo gasto da primeira estação
    return slotPrimeira, slotAtual