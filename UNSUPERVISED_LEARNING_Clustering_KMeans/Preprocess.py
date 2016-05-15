#!/usr/bin/python2.7
# _*_ coding: utf-8 _*_

from Data import Instancia, Atributo
from ServiceManager import ManagerContainer
import constants, random, copy

class ImportInstances(ManagerContainer):
    '''Clase que se encarga de importar las instancias. Pueden provenir de
    3 tipos de ficheros:
    
        1) .arff
            Por cada linea nos vendra @ATTRIBUTE y eso indicará que hay un atributo
            Cuando nos encontremos el atributo @ATTRIBUTE class, eso nos indicará que
            ese fichero viene provisto de una clase. Entre llaves nos vendrán las clases
            posibles. Cuando encontremos la etiqueta @DATA tendremos, por cada fila, una
            instancia
            
            Ejemplo: 
                @ATTRIBUTE controlG NUMERIC
                @ATTRIBUTE controlH NUMERIC
                
                @ATTRIBUTE class {Tumor,Normal}
                @DATA
                8589.416,5468.2407, Tumor
            
        2) .csv
            Tendremos un header que nos dirá cada uno de los atributos que compone
            cada instancia. Si tiene clase, vendrá informada como el último atributo.
            Cada atributo viene separado por comas (,) y en cada línea habrá una instancia
            Si hay una # o un % quiere decir que esa línea es un comentario. Asumimos
            que la primera línea después de los comentarios contendrá el encabezado
            y las siguientes líneas serán las instancias
            
            Ejemplo: 
            % this file is available through: http://facweb.cs.depaul.edu/mobasher/classes/ect584/weka/k-means.html
            id,age,sex,region,income,married,children,car,save_act,current_act,mortgage,pep
            ID12101,48,FEMALE,INNER_CITY,17546.0,NO,1,NO,NO,NO,NO,YES
            ID12102,40,MALE,TOWN,30085.1,YES,3,YES,NO,YES,YES,NO
            
        3) .txt
            Tendremos un fichero (.atributos.txt) que contendrá, por cada línea, los
            atributos de una instancia.
            [OPCIONAL] Tendremos otro fichero (.clase.txt) que contendrá, por cada línea, 
            la clase a la que pertenece una instancia.
            
            Si no nos encontramos ante este formato, nuestro programa lanzará un error
            '''
    def __init__(self, manager):
        '''
        Constructor
        '''
        ManagerContainer.__init__(self, manager)

    def getInstances(self):
        extensionFile = self._getManager().getConfiguration().getFileExtension()
        instancias = None
        if(extensionFile == constants.EXT_ARFF):
            instancias = self._getArffInstances()
        elif(extensionFile == constants.EXT_CSV):
            instancias = self._getCsvInstances()
        elif(extensionFile == constants.EXT_TXT):
            instancias = self._getTxtInstances()
        else:
            True
            ##ERROR
        return instancias
    
    def _getArffInstances(self):
        fichero = self._getManager().getConfiguration().getInputFile()
        fichero = self._getManager().getFiles().openFile(fichero)
        datosEncontrados = False #Si hemos encontrado el label @DATA
        listaAtribs = []
        listaInstances = []

        #Nos recorremos el fichero
        for linea in fichero: 
            if not (datosEncontrados): 
                #Si encontramos la etiqueta atributo obtenemos el atributo
                '''
                @ATTRIBUTE controlH NUMERIC

                @ATTRIBUTE class {Tumor,Normal}
                @DATA
                ...
                '''
                attribPos = linea.find(constants.LABEL_ATTR or constants.LABEL_ATTR.lower())
                
                if (attribPos!=-1):
                    attribNameInicial = linea.find(constants.BLANK_SPACE, attribPos)+1
                    attribNameFinal = linea.find(constants.BLANK_SPACE, attribNameInicial)
                    nombreAttr = linea[attribNameInicial:attribNameFinal].strip(constants.STRIP)
                    typeAttr = linea[attribNameFinal+1:].strip(constants.STRIP)
                    a = Atributo(nombreAttr, typeAttr)
                    listaAtribs.append(a)
                #Si no la encontramos, buscamos la etiqueta DATA
                else:
                    if((linea.find(constants.LABEL_DATA)!=-1) or (linea.find(constants.LABEL_DATA.lower())!=-1)):
                        datosEncontrados = True
            else:
                '''
                @ATTRIBUTE name type 
                
                @DATA --> nos encontramos aqui, la sig linea es la que tenemos que leer para
                obtener las instancias
                ...
                '''
                lineaTerminada = False
                instancia = Instancia()
                i= 0
                while(lineaTerminada == False): #mientras la linea no este terminada
                    leerDesde = 0
                    leerHasta= linea.find(constants.COMA) #buscamos la siguiente coma
                    #cogemos el nombre y tipo del atributo q nos toca leer
                    if(leerHasta==-1):            
                        lineaTerminada = True
                        leerHasta = len(linea)-1
                    atributo = copy.copy(listaAtribs[i])
                    valorAtrib = linea[leerDesde:leerHasta]
                    atributo.setValor(valorAtrib) #definimos el valor del atributo
                    instancia.addAtributo(atributo) #lo aniadimos a la instancia
                    linea = linea[leerHasta+1:]  #actualizamos la linea
                    i+=1
            
                instancia.setNumAtributosNumericos()
                listaInstances.append(instancia)
                    #hay que tener en cuenta que la primera linea de data, no contiene datos
                    
        self._getManager().getFiles().closeFile(fichero) #una vez leido el fichero, lo cerramos
        return listaInstances
        
#    def _getCsvInstances(self):
        
#    def _getTxtInstances(self):
           
class Preproceso(ManagerContainer):
    def __init__(self, manager):
        '''
        Constructor
        '''
        ManagerContainer.__init__(self, manager)
    
    def randomize(self, instancias):
        #metodo que randomiza la lista
        random.shuffle(instancias)
        return instancias
    
    def normalize(self, instancias):
        #metodo que normaliza los atributos
        '''
        Xnew = (X - Xmin)/(Xmax - Xmin)
        
        Para cada instancia y para cada atributo, cogemos el menor y el mayor.
        Para cada instancia y para cada componente, hacemos la formula de Xnew.
        '''
        #Obtener los atributos numericos SOLO
        #PRECONDICION: Los atributos tienen que ser positivos
        for i in range(instancias[0].getNumAtributos()):
            xmax = 0
            xmin = 0
            primeraVuelta = True
            #Obtenemos el maximo y el minimo
            for instancia in instancias:
                if not(instancia.getAtributo(i).isNominal()):
                    if(primeraVuelta):
                        xmax = instancia.getAtributo(i).getValor();
                        xmin = xmax #Si es la primera vuelta, inicializamos xmin
                        primeraVuelta = False
                    else:
                        if(instancia.getAtributo(i).getValor()>xmax):
                            xmax = instancia.getAtributo(i).getValor()
                        elif(instancia.getAtributo(i).getValor()<xmin):
                            xmin = instancia.getAtributo(i).getValor()
                else:
                    break #si es nominal, salimos del for (no nos recorremos ese atributo)
                        
            for instancia in instancias:
                #Aplicamos la formula
                #Xnew = (X - Xmin)/(Xmax - Xmin)
                if not(instancia.getAtributo(i).isNominal()):
                    numerador = instancia.getAtributo(i).getValor() - xmin
                    denominador = xmax - xmin
                    instancia.getAtributo(i).setValor(numerador/denominador)  
                else:
                    break #si es nominal, salimos del for (no nos recorremos ese atributo)
        return instancias