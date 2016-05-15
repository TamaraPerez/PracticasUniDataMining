from Vecino import Vecino
class KVecinosMasProximos(object):
    '''
    classdocs
    '''


    def __init__(self, k):
        self._listKVecinos = []
        self._numVecinosAExplorar = k
        
    def getListaVecinos(self):
        return self._listKVecinos;
    
    def getLen(self):
        return int(len(self._listKVecinos))
    
    def addVecino(self, vecino): 
        '''
        Este metodo aniadira al vecino mas proximo (con su distancia calculada), siempre y cuando
        corresponda aniadirlo.
        
        Solo corresponde aniadirlo si la distancia desde la instancia en cuestion a la instancia de la cual
        queremos predecir la clase es MENOR que alguna de las que hay en la lista, sino, no la aniadiremos
        '''
        
        if(self._numVecinosAExplorar>=len(self._listKVecinos)):
            self._listKVecinos = sorted(self._listKVecinos, key=lambda vecino: vecino.getDistancia()) 
            if(self._esDistanciaSuperiorALasDeLaLista(vecino)==False):             
            #si hay en la lista menos vecinos que la k (numero de vecinos disponibles) 
            # y si la distancia de ese vecino, es inferior a la lista de vecinos q tiene la instancia:
                self._listKVecinos.append(vecino) #se aniade al final de la lista el vecino

            #ordenamos la lista de menor a mayor en funcion de la distancia
        
    def _esDistanciaSuperiorALasDeLaLista(self, vecino):
        #metodo que comprueba si la distancia del vecino es menor a alguna de las que hay en la lista
        esMayor = True #suponemos que no va a entrar en la lista de los k vecinos cercanos
        i=0
        while (len(self._listKVecinos)>i and esMayor==True):
            #mientras siga habiendo elementos en la lista de los k vecinos cercanos, y no hayamos 
            #    detectado que la distancia del vecino es menor que las de la lista 
            if(len(self._listKVecinos)<self._numVecinosAExplorar):
                esMayor = False
            #elif(len(self._listKVecinos)==self._numVecinosAExplorar):
            elif(self._listKVecinos[i].getDistancia()>vecino.getDistancia()):
                #si la distancia del vecino es menor que la de alguno de la lista
                self._listKVecinos.pop(self._numVecinosAExplorar-1); #eliminamos el ultimo elemento de la lista (el mas mayor)
                esMayor = False
            i+=1
        if(len(self._listKVecinos)==0):
            esMayor = False
        return esMayor    