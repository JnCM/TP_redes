#coding: utf-8

#Classe que define uma estação da simulação
class Estacao:

    #Construtor da classe
    def __init__(self, idEstacao):
        #Atributo responsável por armazenar o identificador de uma estação
        self.idEstacao = idEstacao
        #Atributo responsável por armazenar o slot de transmissão correspondente de uma estação
        self.slot = 1
        #Atributo responsável por indicar se uma estação transmitiu seu quadro
        self.transmitiu = 0
    
    #Método que altera o valor do slot de uma estação
    def setSlot(self, novoSlot):
        self.slot = novoSlot
    
    #Método que altera o valor da flag que indica se uma estação transmitiu
    def setTransmitiu(self):
        self.transmitiu = 1
    
    #Método que retorna o identificador de uma estação
    def getIdEstacao(self):
        return self.idEstacao

    #Método que retorna o respectivo slot de uma estação
    def getSlot(self):
        return self.slot
    
    #Método que retorna a flag de transmissão de uma estação
    def getTransmitiu(self):
        return self.transmitiu
