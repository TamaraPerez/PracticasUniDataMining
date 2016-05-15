#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from time import strftime, gmtime
import os

NUM_MAX_ARGS = 12
ERROR_ARGS= 'Ha introducido un número superior de argumentos. Revise el README.txt para más información.'
EXT_ARFF ='.arff'
EXT_TXT = '.txt'
EXT_CSV = '.csv'
LABEL_ATTR = '@ATTRIBUTE' #hacer que le de igual mayus o minus!!!
LABEL_DATA = '@DATA' #hacer que le de igual mayus o minus!!!!
BLANK_SPACE = ' '
COMA = ','
PUNTO = '.'
LABEL_CLASS = 'class'
FINAL_LINE= '\n'
NOMBRE_CLUSTER = 'cluster_'
ATTR_TYPE_NOMINAL = 'string'
NORMALIZE_MIN = 0
NORMALIZE_MAX = 1
HALT_ITERATIONS = 0
HALT_UMBRAL = 1
HALT_NUM_ITERATIONS =5
HALT_PORCENTAJE_UMBRAL=0.05 #5%
STRIP = ' \t\n\r'
#TRAZAS
DEFAULT_TRACES_PATH = os.path.dirname(__file__) +'/traces/trace_'
DEFAULT_TRACES_FILETYPE = '.txt'
DEFAULT_TRACES_FILE = DEFAULT_TRACES_PATH+strftime("%Y-%m-%d", gmtime()).replace(' ', '_')+DEFAULT_TRACES_FILETYPE
INFO_TRACE='INFO: '
WARNING_TRACE='WARNING: '
ERROR_TRACE='ERROR: '

#MENSAJES
MSG_INITIALIZATION_INPUT_FILE = 'El fichero de entrada es: '
MSG_INITIALIZATION_OUTPUT_FILE = 'El fichero de salida es: '
MSG_INITIALIZATION_K = 'El número de clusters es: '
MSG_INITIALIZATION_M = 'El valor de la m de Minkowski utilizado es: '
MSG_INITIALIZATION_H = 'El criterio de parada utilizado es [0: Número de iteraciones fijo/1: Umbral de error]: '
MSG_INITIALIZATION_INIT = 'El tipo de inicialización utilizada es [0: Centroides aleatorios/1: Por división del espacio]: '
SALTO_DE_LINEA = '\n'
MSG_RUNTIME = 'El tiempo de ejecución ha sido de: '
RUNTIME_UNIDADES = 's '
NUM_OF_CLUSTERS = 'El número de clusters es: '
NUM_OF_INSTANCES = 'El número de instancias leídas es: '
NUM_OF_ATRIBS = 'El número de atributos por cada instancia es: '
NUM_OF_ATRIBS_NUMERICS = 'El número de atributos numéricos por cada instancia es: '
MSG_CENTROIDES = 'El centroide del '
MSG_INSTANCIA = 'Instancia_'
MSG_DOSPUNTOS_SEPARACION= ' pertenece al cluster: '
ATRIBS_INSTANCIA = 'sus atributos son: '