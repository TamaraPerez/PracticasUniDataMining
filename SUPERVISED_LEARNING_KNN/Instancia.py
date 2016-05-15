class Instancia(object):
    '''
    classdocs
    '''

    #una instancia se caracteriza por una lista de atributos y la clase
    def __init__(self):
        self._listAtributos = []
        #+self._clase
        #self._clasePredicha  
        #self._vecinosMasProximos
        
    def addAtributo(self, atributo):
        a=float(atributo)
        self._listAtributos.append(a)
        
    def getValor(self):
        return self._valor
    
    def setClase(self, pClase):
        self._clase = pClase
    
    def imprimir(self):
        print(self._clase)
    
    def getLenVecinos(self):
        return self._kVecinosMasProximos.getLen()
    
    def getNumAtributos(self):
        return len(self._listAtributos)
    
    def getClase(self):
        return self._clase
    
    def getClasePredicha(self):
        return self._clasePredicha
    
    def getAtributo(self, posAtributo):
        return self._listAtributos[posAtributo]
    
    def setClasePredicha(self, pClase):
        self._clasePredicha = pClase
    
    def getKVecinosMasProximos(self):
        return self._kVecinosMasProximos.getListaVecinos()
        
    def setKVecinosMasProximos(self, pKVecinosMasProx):
        self._kVecinosMasProximos = pKVecinosMasProx