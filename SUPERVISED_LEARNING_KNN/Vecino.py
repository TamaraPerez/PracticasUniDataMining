class Vecino(object):
  
    def __init__(self, instanciaCercana):
        self._distancia = 0.0 #distancia de la instancia de train a la de test
        self._instancia = instanciaCercana #instancia de train

    def calcularDistancia(self, m, i1):
        for i in range(i1.getNumAtributos()): 
            #calculamos la distancia entre 2 instancias, segun la formula de minkowski
            self._distancia = (abs(i1.getAtributo(i)-self._instancia.getAtributo(i)))**m + self._distancia
        self._distancia = self._distancia**(1/m)
            
    def getDistancia(self):
        return self._distancia
    
    def getClaseInstancia(self):
        return self._instancia.getClase()