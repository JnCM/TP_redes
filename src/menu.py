#coding: utf-8

#Menu de opções da simulação
def menu():
    algoritmo = -1
    while algoritmo == -1:
        print("--------------------- Selecione qual algoritmo utilizar ---------------------")
        print("| 1 - Slotted Aloha;                                                        |")
        print("| 2 - CSMA p-persistente;                                                   |")
        print("| 3 - Recuo binário exponencial;                                            |")
        print("| 0 - Sair.                                                                 |")
        print("-----------------------------------------------------------------------------")
        algoritmo = int(input())
        if algoritmo != 0 and algoritmo != 1 and algoritmo != 2 and algoritmo != 3:
            algoritmo = -1
    
    if algoritmo != 0:
        n = -1
        while n == -1:
            print("---------------------- Selecione o número de estações -----------------------")
            print("| 1 - 20;                                                                   |")
            print("| 2 - 40;                                                                   |")
            print("| 3 - 100;                                                                  |")
            print("| 0 - Sair.                                                                 |")
            print("-----------------------------------------------------------------------------")
            n = int(input())
            if n != 0 and n != 1 and n != 2 and n != 3:
                n = -1
            elif n == 1:
                n = 20
            elif n == 2:
                n = 40
            elif n == 3:
                n = 100
    
    if n == 0 or algoritmo == 0:
        return 0, 0
    else:
        return algoritmo, n
    