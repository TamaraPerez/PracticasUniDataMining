#!/usr/bin/python2.7
# _*_ coding: utf-8 _*_

import constants

class Instancia(object):
    '''
    classdocs
    '''

    def __init__(self):
        self._atributos = []
        self._clase = None
        self._numAtributosNumericos=0
        #Lista de los clusters a los que pertenece con probabilidad p
        #Lo podremos ampliar para hacer tanto clustering exclusivo como probabilistico
        self._pertenencias = [] 
        
    def addAtributo(self, atributo):
        self._atributos.append(atributo)
    
    def isAssignedToCluster(self, cluster):
        encontrado = False
        i=0
        while not (encontrado or i>=len(self._pertenencias)):
            if (self._pertenencias[i].getCluster() == cluster):
                encontrado = True
            else:
                i+=1
        return encontrado
        
    def calcularDistanciaMinkowski(self, m, coordenadas):
        distancia = 0
        #si el numero de coorderadas es igual que el numero de atributos numericos... 
        if (self._numAtributosNumericos == len(coordenadas)):
            i=0
            #para cada atributo de la instancia calculamos la distancia minkowski
            for atr in self._atributos: 
                #calculamos la distancia entre 2 puntos, segun la formula de minkowski
                if not (atr.isNominal()):
                    #si el atributo es nominal, calculamos su distancia
                    distancia = (abs(coordenadas[i].getValor()-atr.getValor()))**m + distancia
                    i+=1
            distancia = distancia**(1.0/float(m))
        return distancia
        
    def setClase(self, clase):
        self._clase = clase
        
    def addPertenencia (self, cluster, probabilidad):
        pertenencia = Pertenencia()
        pertenencia.setCluster(cluster)
        pertenencia.setProbabilidad(probabilidad)
        self._pertenencias.append(pertenencia)

    def getCluster(self):
        return self._pertenencias[0].getCluster() #como es EXCLUSIVO, nos sirve devolver la primera posicion
    
    def clearPertenencias (self):
        self._pertenencias = []
       
    def getClase(self):
        return self._clase
    
    def getNumAtributos(self):
        return len(self._atributos)
      
    def getNumAtributosNumericos(self):
        return self._numAtributosNumericos
        
    def setNumAtributosNumericos(self):
        num=0
        for at in self._atributos:
            if not (at.isNominal()):
                num+=1
        self._numAtributosNumericos=num
    
    def getAtributos(self):
        return self._atributos
        
    def getAtributo(self, posicion):
        return self._atributos[posicion]
        
class Atributo(object):
    '''
    classdocs
    '''

    def __init__(self, nombreAttr, tipo):
        self._nombre = nombreAttr
        self._tipo = tipo
        self._valor = None
        
    def getNombre(self):
        return self._nombre
    
    def setValor(self, value):
        
        #si el tipo no es nominal, lo convertimos a float (porque sera numerico)
        if not (self.isNominal() or self._nombre == constants.LABEL_CLASS):
            self._valor = float(value)
        else:
            self._valor = value
        

    def getValor(self):
        return self._valor

    def getClass(self):
        True
        #En el caso de ser necesario, devolver lista de clases. Ej. {blabla, blabla}
        #nombre = class
        
    def isNominal(self):
        nominal = False
        if(self._tipo==constants.ATTR_TYPE_NOMINAL or self._nombre==constants.LABEL_CLASS):
            nominal = True
        return nominal
        
    def getTipo(self):
        return self._tipo
    
class Cluster(object):
    
    def __init__(self, nombre):
        self._posCentroide = [] #tendremos una lista porque habra tantos numeros como atributos (2.3, 5.6, 1.1)
        self._posCentroideTemp =[]
        self._nombre = constants.NOMBRE_CLUSTER + str(nombre)
        
    def getPosCentroide(self):
        return self._posCentroide
        
    def getNombre(self):
        return self._nombre
    
    def clearPosicionCentroide(self):
        self._posCentroide = []
    
    def clearPosicionCentroideTemp(self):
        self._posCentroideTemp = []
    
    def sumarValorComponente(self, dimension, valor):
        #ya sabemos que no es nominal
        self._posCentroide[dimension].setValor(self._posCentroide[dimension].getValor()+valor)
        
    def setValorComponente(self, dimension, valor):
        self._posCentroide[dimension].setValor(valor)
        
    def getValorComponente(self, dimension):
        return self._posCentroide[dimension].getValor()
    
    def getValorComponenteTemp(self, dimension):
        return self._posCentroideTemp[dimension].getValor()
    
    def setPosicionCentroideTemp(self, posNueva):
        self._posCentroideTemp = posNueva
        
    def setPosicionCentroide(self, posNueva):
        posCorrecta = []
        for coord in posNueva:
            if not (coord.isNominal()):
                posCorrecta.append(coord)
        self._posCentroide = posCorrecta
    
class Pertenencia(object):
    
    def __init__(self):
        self._cluster = None
        self._probabilidad = 0.0
        
    def setProbabilidad(self, p):
        self._probabilidad = p
        
    def getProbabilidad(self):
        return self._probabilidad
    
    def setCluster(self, cl):
        self._cluster = cl
        
    def getCluster(self):
        return self._cluster