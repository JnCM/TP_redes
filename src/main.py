#coding: utf-8

from menu import menu
from utils import inicializa, calculaResultado
from slottedAloha import slottedAloha
from csmaPPersistente import csmaPPersistente

if __name__ == "__main__":
    slots = []
    slotsPrimeira = []
    nomeAlgoritmo = ''
    algoritmo, n = menu()
    if algoritmo != 0 and n != 0:
        if algoritmo == 1:#Executa Slotted Aloha
            nomeAlgoritmo = "Slotted Aloha"
            for i in range(33):
                slotPrimeira, slot = slottedAloha(inicializa(n), n)
                slots.append(slot)
                slotsPrimeira.append(slotPrimeira)
        elif algoritmo == 2:#Executa CSMA p-persistente
            nomeAlgoritmo = "CSMA p-persistente"
            for i in range(33):
                slotPrimeira, slot = csmaPPersistente(inicializa(n), n)
                slots.append(slot)
                slotsPrimeira.append(slotPrimeira)
        elif algoritmo == 3:#Executa Recuo binário exponencial
            nomeAlgoritmo = "Recuo binário exponencial"
            print("Recuo binário exponencial!")

        print("\nAlgoritmo: {}".format(nomeAlgoritmo))
        calculaResultado(slots, slotsPrimeira)

