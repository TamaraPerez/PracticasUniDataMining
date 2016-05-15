#!/usr/bin/python2.7
# _*_ coding: utf-8 _*_

from Preproceso import Preproceso
from DataFiles import DataFiles
from Evaluacion import Evaluacion
from KNN import KNN
from datetime import datetime
import sys;

'''
ALGORITMO (kNN)
---------
1) TRAINING: Almacenamos cada instancia de entrenamiento en una lista (training_list)
2) CLASSIFICATION
    2.1) Dada una instancia de la cual queremos predecir la clase
        2.1.1) obtenemos la distancia a cada una de las instancias ####lista_distancias<-getDistanciaACadaInstancia(instancia, m)
            |NO::::2.1.1.1) por cada instancia 'i' de la training_list: 
            |NO::::        lista_distancias<-calcularDistanciaMinkowski(instancia, training_list[i], m)
            |NO::::        return lista_distancias
        2.1.2) ordenar las distancias #####sort(lista_distancias)
        2.1.3) obtener las k-instancias con distancia minimas
    2.2) Etiquetamos la instancia con la clase mayoritaria
'''

if __name__ == '__main__':  #main
    start_time = datetime.now()
    data = DataFiles()          
    preproceso = Preproceso()
    evaluacion = Evaluacion()
    try:
        #1. LEER FICHERO
        inputPath = sys.argv[1];
        input_instances = data.obtenerInstanciasDeFichero(inputPath)  #1.2 cargamos el fichero
        input_instances.calcNumClases()
        #2. PREPROCESO
        preproceso.randomizarInstancias(input_instances)
        
        #3. kNN
        #70% instancias con clase, 30% instancias a clasificar
        k = int(sys.argv[2]) #num de vecinos a explorar
        m = float(sys.argv[3]) #m de la dist de Minkowski
        porcentaje = sys.argv[4]
        porcentaje = float(porcentaje)
        if(porcentaje>100.0 or porcentaje<0.0):
            raise Exception()
        train = input_instances.getPorcentaje(porcentaje) #obtenemos el % de las instancias (para train) 
        test = input_instances #lo restante (test) (el getPorcentaje actualiza la lista haciendo pop())
        print("Usando k="+str(k)+", m="+str(int(m))+" y usando el " + str(porcentaje) +"% de las instancias para train\n")
        print("Clasificando...")
        
        clasificador = KNN(train, test, k, m) #creamos el clasificador con las instancias de las q sabemos la clase, las q queremos predecir la clase, k, m
        clasificador.execute() #calculamos los vecinos proximos, y predecimos la clase
        prediccion = clasificador.getPrediccion()
        
        #4. EVALUACION    
        evaluacion.mostrarFigurasMerito(prediccion, input_instances) #Specificity y Recall
        #evaluacion.espacioROC() #representar graficamente los modelos en el espacio ROC.
        time = str(datetime.now()-start_time)
        time = time[5:]
        print("Duración de la ejecución del programa: " + time + " segundos")
    except (IOError):
        print("Error de lectura de fichero")
    #except(Exception):
        #print("Error desconocido. Seguramente hayas introducido incorrectamente algún argumento")