#!/usr/bin/python2.7
# _*_ coding: utf-8 _*_

from time import gmtime, strftime, clock
import constants, os

class ManagerContainer(object):
    
    def __init__(self, m):
        self._manager = m
        
    def _getManager(self):
        return self._manager

#Class Manager: Inicia los servicios requeridos (en este caso el de trazas y el de configuracion)
class Manager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._traces = Traces()
        self._configuration = Configuration()
        self._files = Files()
  
    def getTraces(self):
        return self._traces
    
    def getConfiguration(self):
        return self._configuration
  
    def getFiles(self):
        return self._files
    
#Class Traces: Servicio de trazas
class Traces(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._tracesFile = None
        self._printTraces = False
        
    def setPrintTraces(self, printTraces):
        self._printTraces = printTraces
    
    def setTracesFile(self, ficheroTrazas):
        self._tracesFile = ficheroTrazas
        
    def printTraceInfo(self, message):
        self._printTrace(message, constants.INFO_TRACE)    
        
    def printTraiceWarning(self, message):
        self._printTrace(message, constants.WARNING_TRACE) 

    def printTraceError(self, message):
        self._printTrace(message, constants.ERROR_TRACE)
        
    def _printTrace(self, message, traceType):
        try:
            fich = open(self._tracesFile,"a+")
            fich.write(traceType + strftime("%Y-%m-%d %H:%M:%S", gmtime())+' '+message+'\n')
            fich.close()
        except IOError:
            raise Exception('IOError al escribir las trazas')
        
        if(self._printTrace):
            print(traceType + strftime("%Y-%m-%d %H:%M:%S", gmtime())+' '+message+'\n')    
        
#Class Configuration: Configuracion general (path de los ficheros obtenidos por los argumentos)      
class Configuration(object):
    '''
        __.py -file [fichero][class/ficheroClase] -k [num] -m [num] -init [num] -h [num] 
        
        use of args:
            -file: fichero de entrada. Y tiene o no clase
            -k: numero de clusters
            -m: distancia de minkowski
            -init: tipo de inicializacion  
            -h: criterio de parada (tipo de convergencia)       
    '''


    def __init__(self):
        '''
        Constructor
        '''  
        self._inputFile = None
        self._inputClass = None
        self._k = None
        self._m = None
        self._inicializacion = None
        self._h = None
        
        self._initialTime = None
        self._finalTime = None
        
    def getInputFile(self):
        return self._inputFile
    
    def setInputFile(self, inputFile):
        self._inputFile = inputFile
        
    def getInputClass(self):
        return self._inputClass
    
    def setInputClass(self, inputClass):
        self._inputClass = inputClass
    
    def setOutputFile(self, fichero):
        self._outputFile = fichero
        
    def getOutputFile(self):
        return self._outputFile
    
    def getK(self):
        return self._k
    
    def setK(self, pK):
        self._k = pK
 
    def getM(self):
        return self._m
    
    def setM(self, pM):
        self._m = pM
    
    def getH(self):
        return self._h
    
    def setH(self, pH):
        self._h = pH        
   
    def getInicializacion(self):
        return self._inicializacion
    
    def setInicializacion(self, pInit):
        self._inicializacion = pInit   
        
    def setInitialTime(self):
        self._initialTime = clock()
        
    def setFinalTime(self):
        self._finalTime = clock()
        
    def getFileExtension(self):
        extension = None
        if(self._inputFile.endswith(constants.EXT_ARFF)):
            extension = constants.EXT_ARFF
        elif(self._inputFile.endswith(constants.EXT_CSV)):
            extension = constants.EXT_CSV
        elif(self._inputFile.endswith(constants.EXT_TXT)):
            extension = constants.EXT_TXT
    
        return extension
    def runtime(self):
        return self._finalTime - self._initialTime   
    
class Files(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def openFile(self, fichero):
        #metodo para abrir el fichero
        return open(fichero, 'r')  
    
    def closeFile(self, fichero):
        fichero.close()

