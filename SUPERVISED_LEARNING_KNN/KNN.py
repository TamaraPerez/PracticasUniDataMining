from KVecinosMasProximos import KVecinosMasProximos
from Vecino import Vecino

class KNN(object):
    '''
    classdocs
    '''


    def __init__(self, inp, pred, pK, pM):
        '''
        Constructor
        '''
        self._train = inp #las instancias con las que realizaremos predicciones
        self._test = pred #las instancias a predecir
        self._k = pK #num de vecinos a explorar
        self._m = pM #distancia de Minkowski con valor m
        
        
    def execute(self):
        '''
        Ejecuta el kNN. Pasos:
        1) Para cada instancia a predecir, calcula la distancia a todas las de "entrenamiento"
        for...(_instancia(instAPredecir)) <--- [Es decir,llamamos a ese metodo por cada instancia a predecir]
        2) Metodo _distancia(instAPred): Le pasamos como parametro la instancia de la cual queremos predecir
        la clase. Este metodo cogera cada una de las instancias de entrenamiento
        '''
        #calculamos los k vecinos cercanos de todas las instancias
        for instanceToPredict in self._test.getInstancias(): 
            #calcula la distancia de cada una de las instancias a predecir a todas las demas
            self._distancia(instanceToPredict)
            #calculamos la clase que le corresponderia a cada instancia
            self._obtenerClase(instanceToPredict)

    def _distancia(self, inst1):
        #metodo que calcula los k vecinos cercanos de una instancia
        kvecinosMasProxAInst1 = KVecinosMasProximos(self._k) #creamos una clase que contiene una lista de los k vecinos mas cercanos
        for inst2 in self._train.getInstancias(): #nos recorremos las instancias
            #creamos un objeto que nos dira a que distancia esta inst1 de inst2 y guarde la clase de inst2
            v = Vecino(inst2) #creamos el vecino con el q miraremos si esta en los k cercanos
            v.calcularDistancia(self._m, inst1)  #calculamos la distancia entre inst1 e inst2
            kvecinosMasProxAInst1.addVecino(v) #aniadimos el vecino en el q caso de q proceda
        inst1.setKVecinosMasProximos(kvecinosMasProxAInst1) #asignamos a la instancia la lista de los k vecinos
    
    def getPrediccion(self):
        return self._test
    
    
    def _obtenerClase(self, instanceToPredict):
        #htVecino[clase]=numApariciones
        htClases = {}
        for vecino in instanceToPredict.getKVecinosMasProximos():
            if(vecino.getClaseInstancia() not in htClases):
                htClases[vecino.getClaseInstancia()] = 1
            else:
                htClases[vecino.getClaseInstancia()] = htClases[vecino.getClaseInstancia()]+1
        clasePredicha = max(htClases, key=htClases.get)
        instanceToPredict.setClasePredicha(clasePredicha)
