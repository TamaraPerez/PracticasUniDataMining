#!/usr/bin/python2.7
# _*_ coding: utf-8 _*_
'''

@author: eka02
'''

import sys, argparse, constants
from ServiceManager import Manager, ManagerContainer
from AlgoritmosUnsupervised import KMeans
from Preprocess import ImportInstances, Preproceso

class Main(ManagerContainer):
    
    def __init__(self):
        '''
        Constructor
        '''
        ManagerContainer.__init__(self, Manager())
        
    '''This is the first method which is called when the app runs'''        
    def main(self):
        #Retrieving args value
        '''
        __.py -file [fichero][class/ficheroClase] -k [num] -m [num] -init [num] -h [num] 
        
        use of args:
            -i: fichero de entrada. Y tiene o no clase
            -o: fichero de salida
            -k: numero de clusters
            -m: distancia de minkowski
            -init: tipo de inicializacion  
            -h: criterio de parada (tipo de convergencia) 
            [-v]: imprime las trazas en la consola     
        '''
        
        self._getArgs()
        self._run()
        
    def _run(self):
        importation = ImportInstances(self._getManager())
        preprocess = Preproceso(self._getManager())
        kmeans = KMeans(self._getManager())
        self._getManager().getConfiguration().setInitialTime()
        
        #0. Obtenemos las instancias
        self._getManager().getTraces().printTraceInfo('Se obtienen las instancias')
        instancias = importation.getInstances()
        #1. PREPROCESO
        self._getManager().getTraces().printTraceInfo('Se inicia el preproceso')
        #1.1 Randomizar las instancias (no obligatorio)
        self._getManager().getTraces().printTraceInfo('Se randomizan las instancias')
        instancias = preprocess.randomize(instancias)
        #1.2 Normalizar los atributos (no obligatorio)
        self._getManager().getTraces().printTraceInfo('Se normalizan las instancias')
        instancias = preprocess.normalize(instancias)
        #2. Algoritmo
        self._getManager().getTraces().printTraceInfo('Comienza la ejecución del kMeans')
        self._getManager().getConfiguration().setInitialTime()
        kmeans.setInstancias(instancias)
        kmeans.run()     
        self._getManager().getConfiguration().setFinalTime()   
        self._getManager().getTraces().printTraceInfo('Finaliza la ejecución del kMeans')
        self._getManager().getTraces().printTraceInfo('El tiempo de ejecución ha sido de: '+str(self._getManager().getConfiguration().runtime()))
        #5 Imprimir resultados
        self._getManager().getTraces().printTraceInfo('Se imprimen los resultados')
        kmeans.imprimirResultados()
        
    
    def _getArgs(self):
        '''#Por defecto, el servicio de trazas no escribe en consola
        tracesConsole = False
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--verbose', help='Activa las trazas en consola', action='store_true')
        parser.add_argument('')
        
        #Obtenemos los argumentos introducidos
        for arg_num in range(len(sys.argv)):
            #Si hay mas argumentos que los requeridos, lanzamos error
            if(len(sys.argv)>constants.NUM_MAX_ARGS):
                print(constants.ERROR_ARGS)   
            else:
                input=sys.argv[arg_num]
                #PENDIENTE
       '''
        parser = argparse.ArgumentParser(description='arguments for clustering')
        parser.add_argument('-i','--input', help='input file name',required=True)
        parser.add_argument('-o','--output',help='output file name', required=True)
        parser.add_argument('-k',help='number of clusters', required=True, type=int)
        parser.add_argument('-m','--minkowski',help='minkowski distance', required=True, type=int)
        parser.add_argument('-init','--initialize',help='initialization type (0/1)', required=True, type=int)
        parser.add_argument('-s', '--stop', help='stopping criteria (0/1)', required=True, type=int)
        parser.add_argument('-v','--verbose',help='activate traces in console', required=False, default = False, action="store_true")
        parser.add_argument('-t','--traces', help='file to print traces', required=False, default = constants.DEFAULT_TRACES_FILE)
        
        args = parser.parse_args()
        
        #Almacenamos la configuracion dada por argumentos
        self._getManager().getConfiguration().setInputFile(args.input)
        self._getManager().getConfiguration().setOutputFile(args.output)
        self._getManager().getConfiguration().setK(args.k)
        self._getManager().getConfiguration().setM(args.minkowski)
        self._getManager().getConfiguration().setH(args.stop)
        self._getManager().getConfiguration().setInicializacion(args.initialize)
        self._getManager().getTraces().setPrintTraces(args.verbose)
        self._getManager().getTraces().setTracesFile(args.traces)
        
if __name__ == '__main__': 
    Main().main()


    