from Instancia import Instancia
from Instancias import Instancias

class DataFiles(object):

    def __init__(self):
        self._fichero = None
        
    def _loadFile(self, path):
        #metodo para abrir el fichero
        self._fichero = open(path)  

    def obtenerInstanciasDeFichero(self, inputFile):
        #metodo para obtener las instancias del fichero
        self._loadFile(inputFile) #abrimos el fichero
        instancias = Instancias() #creamos una lista de instancias
        encontrado = False 
        for linea in self._fichero: #nos recorremos todas las lineas del fichero
            if(encontrado == False): 
                if (linea.find('@data')!=-1): 
                    #si encontramos @data, sabemos q apareceran las instancias en la siguiente linea
                    encontrado=True 
            else:
                instancia = Instancia() #creamos una instancia
                self._cargarAtributos(instancia, linea) #insertamos por cada instancia sus atributos
                instancias.addInstancia(instancia) #aniadimos la instancia a la lista de instancias
        self.closeFile() #una vez leido el fichero, lo cerramos
        return instancias
                    
    def _cargarAtributos(self, instancia, linea):
        #metodo que insertara en cada instancia sus atributos
        lineaTerminada = False
        while(lineaTerminada == False): #mientras la linea no este terminada
            leerDesde = 0
            if(linea.find(',')!=-1): #si en esa linea encontramos una coma (la linea se va recortando)
                leerHasta= linea.find(',') #buscamos la siguiente coma
                atributo = linea[leerDesde:leerHasta] #leemos el atributo.
                instancia.addAtributo(atributo) #lo aniadimos a la instancia
                linea = linea[leerHasta+1:]  #actualizamos la linea
            else: #si no encontramos mas comas, hemos terminado y lo siguiente que encontramos es la clase
                lineaTerminada = True
                clase = linea[leerDesde:]
                instancia.setClase(clase)
                
    def closeFile(self):
        self._fichero.close()