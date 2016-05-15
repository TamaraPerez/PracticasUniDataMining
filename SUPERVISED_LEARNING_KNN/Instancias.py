import random
from Instancia import Instancia
class Instancias(object):
    '''
    classdocs
    '''


    def __init__(self):
        self._listInstancias = []
        self._lista_clases = [] #clases que hay en todas las instancias
        
    def getInstancias(self):
        #metodo que devuelve la lista de instancias
        return self._listInstancias
    
    def printNumClases(self):
        print(self._numClases)
        
    def addInstancia(self, instancia):
        #metodo que aniade una instancia a la lista
        self._listInstancias.append(instancia)
        
    def getNumInstancias(self):
        return len(self._listInstancias)
    
    def imprimir(self):
        #metodo que imprime las clases de todas las instancias
        for i in range(len(self._listInstancias)):
            print(self._listInstancias[i].getClase())
            
    def length(self):
        #metodo que devuelve la longitud de la lista
        return len(self._listInstancias)
    
    def getPorcentaje(self, porcentaje):
        #metodo que nos devuelve  la lista de instancias de las q sabremos la clase
        tamanio = (len(self._listInstancias) * (porcentaje/100)) #tamanio del porcentaje en la lista
        tamanio = int(round(tamanio,0)) #quitamos los decimales
        newList = Instancias() #creamos una nueva lista de instancias (para devolver)
        for i in range (tamanio): #para cada instancia de nuestra lista de instancias
            newList.addInstancia(self._listInstancias.pop()) 
            #aniadimos a la nueva lista, la instancia que quitamos
        return newList
            
    def randomize(self):
        #metodo que randomiza la lista
        random.shuffle(self._listInstancias)

    def getListaClases(self):
        return self._lista_clases
    
    def calcNumClases(self):
        numClases = 0
        for instancia in self._listInstancias:
            clase = instancia.getClase()
            if(clase not in self._lista_clases):
                numClases+=1
                self._lista_clases.append(clase)
        self._numClases = numClases
        
    def getNumInstanciasPorClase(self, clase):
        i=0
        for inst in self._listInstancias:
            if(inst.getClase() == clase):
                i+=1
        return i