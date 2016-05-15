# -*- coding: utf-8 -*-
from ServiceManager import ManagerContainer
from Preprocess import Preproceso
from Data import Cluster, Atributo
import constants, copy

class KMeans(ManagerContainer):
    '''
    classdocs
    '''
    #2.1 Inicializacion (aleatorio o division del espacio)
    #2.2 run
    
    #4. Criterio de parada
    #4.1 n iteraciones
    #4.2 umbral max de cambio
    '''
        1. Dadas n instancias, inicializamos k centroides de los clusters (apart.1)
        2. Asignamos cada instancia al centroide más cercano
        3. Actualizamos el centroide para cada cluster
        4. Repetimos el paso 2 y 3 hasta q no cambien los centroides (apart.3)
    '''
    def __init__(self, manager):
        ManagerContainer.__init__(self, manager)
        self._instancias = None
        self._clusters = []
    
    def setInstancias(self, instancias):  
        self._instancias = instancias
        
    def _addCluster(self, cluster):
        self._clusters.append(cluster)
        
    def run(self):
        
        #1. Inicializacion del kmeans
        self._initialize()
        self._kmeansAlgorithm()
    
    def imprimirResultados(self):
        #imprimimos el runtime
        #imprimir las inicializaciones
        #imprimimos el numero de clusters
        #imprimimos el numero de instancias
        #imprimimos el numero de atributos
        #imprimimos los centroides de los clusters
        #imprimimos los las instancias asociadas a cada cluster (inst + i +: + atribs)
        message = ''
        message = self._printInitialization()
        message = message + self._printRuntime()
        message = message + constants.SALTO_DE_LINEA
        message = message + self._printNumOfClusters()
        message = message + self._printNumOfInstances()
        message = message + self._printNumOfAtribs()
        message = message + constants.SALTO_DE_LINEA
        message = message + self._printAtributos()
        message = message + constants.SALTO_DE_LINEA
        message = message + constants.SALTO_DE_LINEA
        message = message + self._printCentroids()
        message = message + constants.SALTO_DE_LINEA
        message = message + constants.SALTO_DE_LINEA
        message = message + self._printInstances()
        print(message)
        open(self._getManager().getConfiguration().getOutputFile(), 'a+').write(message)        
        
    def _printAtributos(self):
        message = ''
        for atributo in self._instancias[0].getAtributos():
            message = message + atributo.getNombre() + ': '+ atributo.getTipo() + constants.SALTO_DE_LINEA
        return message
    
    def _printInitialization(self):
        message = constants.MSG_INITIALIZATION_INPUT_FILE + str(self._getManager().getConfiguration().getInputFile())+constants.SALTO_DE_LINEA
        message = message + constants.MSG_INITIALIZATION_OUTPUT_FILE + str(self._getManager().getConfiguration().getOutputFile())+constants.SALTO_DE_LINEA
        message = message + constants.MSG_INITIALIZATION_K + str(self._getManager().getConfiguration().getK())+constants.SALTO_DE_LINEA
        message = message + constants.MSG_INITIALIZATION_M + str(self._getManager().getConfiguration().getM())+constants.SALTO_DE_LINEA
        message = message + constants.MSG_INITIALIZATION_H + str(self._getManager().getConfiguration().getH())+constants.SALTO_DE_LINEA
        message = message + constants.MSG_INITIALIZATION_INIT + str(self._getManager().getConfiguration().getInicializacion())+constants.SALTO_DE_LINEA
        return message
            
    def _printRuntime(self):
        return constants.MSG_RUNTIME + str(self._getManager().getConfiguration().runtime())+constants.RUNTIME_UNIDADES+constants.SALTO_DE_LINEA
        
    def _printNumOfClusters(self):
        return constants.NUM_OF_CLUSTERS + str(len(self._clusters))+constants.SALTO_DE_LINEA
        
    def _printNumOfInstances(self):
        return constants.NUM_OF_INSTANCES + str(len(self._instancias))+constants.SALTO_DE_LINEA
        
    def _printNumOfAtribs(self):
        message = constants.NUM_OF_ATRIBS + str(self._instancias[0].getNumAtributos())+constants.SALTO_DE_LINEA
        message = message + constants.NUM_OF_ATRIBS_NUMERICS + str(self._instancias[0].getNumAtributosNumericos())+constants.SALTO_DE_LINEA
        return message
        
    def _printAtributosCoordenadas(self, lista):
        message = ''
        primeraVuelta = True
        message = message + '['
        for coord in lista:
            if(primeraVuelta):
                message = message + str(coord.getValor())
                primeraVuelta = False
            else:
                message = message + ', ' +str(coord.getValor())
        message = message + ']'+constants.SALTO_DE_LINEA
        
        return message 
         
    def _printCentroids(self):
        message = ''
        for cluster in self._clusters:
            message = message + constants.MSG_CENTROIDES + cluster.getNombre() +' es '
            message = message + self._printAtributosCoordenadas(cluster.getPosCentroide())
        return message
    
    def _printInstances(self):
        i=1
        message = ''
        for instancia in self._instancias:
            message = message + constants.MSG_INSTANCIA + str(i) + constants.MSG_DOSPUNTOS_SEPARACION +instancia.getCluster().getNombre() +' y ' + constants.ATRIBS_INSTANCIA
            message = message + self._printAtributosCoordenadas(instancia.getAtributos())
            i+=1
        return message
    def _kmeansAlgorithm(self):
        '''
        Metodo que se encarga de ejecutar el kmeansclustering
        '''
        
        '''
        ITERAR
        5) Asociamos a cada centroide las instancias mas cercanas. 
        Para ello calculamos la distancia desde cada una de las instancias a los centroides 
        que hemos inicializado (la distancia se calcula como en el knn)
        6) Calculamos el centro de masas (distancia media entre la instancia 
        más lejana y más cercana de ese cluster).
        7) Paramos cuando hayamos hecho un nº fijo de iteraciones (definido por el programador) 
        o por la diisimilitud engtre codebooks sucesivos 
        menor a un umbral prefijado por el programador. El umbral tiene que ser un %. 
        Para ello, guardaremos para cada centroide su posición anterior.

        '''
        parada = False
        i = 1
        while not (parada):
            #Asociamos a cada instancia su cluster mas cercano
            self._asociarClustersMasCercano()
     
            #Calculamos el centro de masas
            self._calcularCentroMasas()
            
            #Criterio de parada
            parada = self._halt(i)
            
            i+=1
        '''
        Cluster 1 = Inst1, Inst2, Inst3
        centro = (Inst1_x + Inst2_x + Inst3_x, Inst1_y + Inst2_y + Inst3_y,.... )/num_instancias
        
        Inst TIENE cluster_asociado
        para cada cluster
            para cada instancia q tenga ese cluster
                calculamos el centro de masas
                
        1) Nos recorremos todos los atributos de cada dimension (dimension = atributo numerico)
        2) En cada dimension, asignamos a cada cluster el valor de la componente que corresponde
        a esa dimension (suma de todos los componentes de las instancias que pertenecen a ese
        cluster / num_instancias que pertenecen a ese cluster)
        '''
    def _halt(self, i):
        parada = False
        if (self._manager.getConfiguration().getH() == constants.HALT_ITERATIONS):
                if (constants.HALT_NUM_ITERATIONS <= i):
                    parada = True
        elif (self._manager.getConfiguration().getH() == constants.HALT_UMBRAL):
            '''
            Fijando como referencia el punto minimo y el maximo de normalizacion, sabremos
            que % se ha movido cada componente respecto a la iteracion anterior
            '''
            for cluster in self._clusters:
                umbralSuperado = False
                dimension=0
                #Mientras que no superemos el umbral ni las dimensiones del cluster, iteramos
                while not (umbralSuperado or len(cluster.getPosCentroide())>dimension):
                    #Hallamos la diferencia de la posicion del cluster respecto la anterior...
                    diferencia = abs(cluster.getValorComponente(dimension) - cluster.getValorComponenteTemp(dimension))
                    #...y calculamos el porcentaje
                    porcentajeDiferencia = diferencia/constants.NORMALIZE_MAX
                    #Si el max de normalizar es el 100%, la diferencia tendra un porcentaje x
                    if (porcentajeDiferencia > constants.HALT_UMBRAL):
                        umbralSuperado=True
                dimension+=1
            if not (umbralSuperado):
                parada=True
        return parada
                
    def _asociarClustersMasCercano(self):
        '''
        Metodo con el que asociamos una instancia al cluster mas cercano.
        
        Para ello, recorremos las instancias y por cada instancia, aniadimos
        la pertenencia al cluster mas cercano tras calcular la distancia a cada 
        uno de los clusters
        '''
        for instancia in self._instancias:
            distanciaMin = constants.NORMALIZE_MAX
            firstCluster = True
            #Calculamos la distancia a cada uno de los clusters
            for cluster in self._clusters:
                distanciaMinkowski = instancia.calcularDistanciaMinkowski(self._getManager().getConfiguration().getM(), cluster.getPosCentroide())
                if (distanciaMinkowski < distanciaMin or firstCluster):
                    clusterMasCercano = cluster
                    if (firstCluster):
                        firstCluster = False
            instancia.clearPertenencias() #borra todas las pertenencia, porq es CLUSTERING EXCLUSIVO
            instancia.addPertenencia(clusterMasCercano, 1.0) #le asociamos a la instancia su cluster, y con probabilidad 1.0
    
    def _vaciarClusters(self):
        #Limpiamos los clusters y asociamos la posicion del centroide al temporal
        for cluster in self._clusters:
            cluster.setPosicionCentroideTemp(cluster.getPosCentroide())
            cluster.clearPosicionCentroide()
    
    def _calcularCentroMasas(self):

        #self._vaciarClusters()
        instanciaAleatoria = self._instancias[0]
        dimension = 0 #dimension del espacio
        instanciasEnClusters = {} #diccionario que contiene {cluster, numInstanciasEnEseCluster}
        
        # 1) Recorremos los atributos...
        for num in range(instanciaAleatoria.getNumAtributos()):
            # 1) ...de cada dimension
            if not (instanciaAleatoria.getAtributo(num).isNominal()):
                #en cada dimension tenemos un atributo de cada instancia (buscamos ese atributo en cada
                #una de las instancias
                primeraVuelta = True
                for instancia in self._instancias:
                    '''
                    Acumulamos el valor del componente al componente del cluster 
                    Ejemplo: cluster1.valorComponente_x1 = (1.3[inst1_x1] + 2.5[inst2_x1] + 1.5[inst3_x1])
                    '''
                    #Si es la primera vez que entramos, fijamos el valor al primer valor, para luego sumar los demas
                    #Esto sustituye al metodo clear
                    if(primeraVuelta):
                        instancia.getCluster().setValorComponente(dimension, instancia.getAtributo(num).getValor())
                        primeraVuelta = False
                    else: 
                        instancia.getCluster().sumarValorComponente(dimension, instancia.getAtributo(num).getValor())
                    #Si el diccionario no contiene la key, add cluster al dicc
                    if not(instanciasEnClusters.has_key(instancia.getCluster())):
                        dictTemp = {instancia.getCluster(): 1}
                        instanciasEnClusters.update(dictTemp)
                    #Sino, add una instancia a la entrada del diccionario
                    else:
                        instanciasEnClusters[instancia.getCluster()] = instanciasEnClusters[instancia.getCluster()] + 1
                
                #Una vez que terminamos con una dimension, dividimos entre el numero de instancias
                #que hay en esa dimension pertenecientes a ese cluster
                for cluster in instanciasEnClusters.keys():
                    cluster.setValorComponente(dimension, cluster.getValorComponente(dimension)/instanciasEnClusters[cluster]) 
                #Pasamos a la siguiente dimension
                dimension+=1
          
    def _initialize(self):
        '''
        Metodo que llamara a un metodo u otro de inicializacion, dependiendo de los valores
        que se hayan introducido por argumentos
        '''
        #Recuperamos la info de la configuracion introducida por el usuario (args)
        #Si es 0 es aleatorio
        if(self._getManager().getConfiguration().getInicializacion()==0):
            self._initializeAleatorio()
        #Si es 1 es division del espacio
        elif(self._getManager().getConfiguration().getInicializacion()==1):
            self._initializeDivisionEspacio()
            
    def _initializeAleatorio(self):
        '''
        Inicializacion aleatoria
        '''
        #Obtenemos el num de clusters
        k = self._getManager().getConfiguration().getK()
        #randomizamos la lista de instancias para poder obtener instancias aleatorias
        instanciasAleatorias = copy.copy(Preproceso(self._getManager()).randomize(self._instancias))
        while(k>0):
            #creamos el Cluster numCluster
            c = Cluster(k)
            #obtenemos una instancia (de una lista randomizada)
            instanciaAleatoria = instanciasAleatorias[k]
            #la eliminamos de la lista (para no repetir la inicializacion de otro cluster en el 
            #mismo punto
            instanciasAleatorias.remove(instanciaAleatoria)
            #fijamos la posicion del centroide en la posicion en la que se encuentra la instancia
            posicion = copy.copy(instanciaAleatoria.getAtributos())
            c.setPosicionCentroide(posicion)
            #aniadimos el cluster a la lista de clusters
            self._addCluster(c)
            k-=1
            
    def _initializeDivisionEspacio(self):
        '''
        Inicializacion por division del espacio
        '''
        #Obtenemos el num de clusters
        k = self._getManager().getConfiguration().getK()
        self._instancias = Preproceso(self._getManager()).normalize(self._instancias)
        initialPosParticion = float(constants.NORMALIZE_MIN) #0
        finalPosParticion = float(constants.NORMALIZE_MAX)/float(k) #1/k (si k = 2 --> 0.5)
        for particion in range(k):
            #El valor de la primera componente, sera NORMALIZE_MAX/k
            #El valor del resto de componentes sera el medio (NORMALIZE_MAX/2)
            #Ver /../doc/division_espacio.png
            
            #ATENCION: Estamos dividiendo el espacio en funcion de la primera componente (del primer atrib)
            c = Cluster(particion)
            listaComponentes = []
            unaInstancia = self._instancias[0]
            primerAtributoNumerico = True
            for i in range(unaInstancia.getNumAtributos()):
                a = Atributo('Componente_'+str(i),'float')
                if(unaInstancia.getAtributo(i).isNominal() == False):
                    if(primerAtributoNumerico == True):
                        #(0+1/k)/2 --> la mitad. Si k = 2 --> (0+0.5)/2 = 0.25
                        a.setValor((initialPosParticion+finalPosParticion)/2)
                        listaComponentes.append(a)
                        primerAtributoNumerico = False
                    else:
                        #(0+1)/2 --> la mitad del espacio normalizado (para centrar el cluster)
                        a.setValor((constants.NORMALIZE_MAX+constants.NORMALIZE_MIN)/2)
                        listaComponentes.append(a)
            c.setPosicionCentroide(listaComponentes) #set coords del centroide del cluster
            self._addCluster(c) #aniadimos el cluster a la lista de clusters
            initialPosParticion = finalPosParticion
            finalPosParticion = finalPosParticion + constants.NORMALIZE_MAX/k            
            
