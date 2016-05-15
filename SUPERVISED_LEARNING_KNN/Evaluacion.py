class Evaluacion(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def mostrarFigurasMerito(self, test, allInstances):
        matricesConfusion=[]
        for clase in allInstances.getListaClases():
            m = MatrizDeConfusion()
            m.setClase(clase)
            for inst in test.getInstancias():
                if (inst.getClase() == clase):
                    #La real es positiva. Puede ser tp o fn
                    if (inst.getClase() == inst.getClasePredicha()):
                        m._tp+=1.0
                    else:
                        m._fn+=1.0
                else: #la real es negativa. Puede ser fp o tn
                    if (inst.getClase() == inst.getClasePredicha()):
                        m._tn+=1.0
                    else:
                        m._fp+=1.0
            matricesConfusion.append(m)
        
        prec = 0.0
        rec = 0.0 
        fpr = 0.0
        acierta = 0.0
        falla=0.0       
        for matriz in matricesConfusion:
            matriz.calcularFigurasDeMerito()
            acierta = acierta + matriz.get_tp() + matriz.get_tn()
            falla = falla + matriz.get_fn() + matriz.get_fp()
            n = test.getNumInstanciasPorClase(matriz.get_clase()) #num instancias de esa clase en el test
            prec = prec + (n*matriz.get_precision()) #precision
            rec= rec + (n*matriz.get_recall()) #recall
            fpr = fpr + (n*matriz.get_fpr()) #fpr
        
        #Weighted Average (es decir, la media ponderada segun el num de instancias totales del test)
        acierta = acierta/len(allInstances.getListaClases())
        falla = falla/len(allInstances.getListaClases())
        prec = prec / test.getNumInstancias()
        rec = rec / test.getNumInstancias() #eje y
        fpr = fpr / test.getNumInstancias() #eje x
        
        
        #Mostramos las figuras de merito
        print("Precision: "+str(prec)+"%")
        print ("Recall: "+str(rec))
        print("Correctly classified instances")
        print(acierta)
        print("Incorrectly classified instances")
        print(falla)

            
        '''    
        for instancia in test.getInstancias():
            if(instancia.getClasePredicha() == instancia.getClase()):
                aciertos+=1
            else:
                errores+=1
        print("aciertos " + str(aciertos))
        print("errores " + str(errores))
        '''


    def espacioROC(self):
        print("k")
        
class MatrizDeConfusion(object):
        
        def __init__(self):
            self._tp=0.0
            self._fp=0.0
            self._tn=0.0
            self._fn=0.0
            self._precision=0.0
            self._recall=0.0
            self._fpr=0.0

        def get_precision(self):
            return self._precision

        def get_recall(self):
            return self._recall

        def get_tp(self):
            return self._tp

        def get_fp(self):
            return self._fp

        def get_tn(self):
            return self._tn

        def get_fn(self):
            return self._fn

        def get_clase(self):
            return self._clase
   
        def get_fpr(self):
            return self._fpr
        
        def setClase(self, pclase):
            self._clase = pclase
        
        def calcularFigurasDeMerito(self):
            self._obtenerPrecision()
            self._obtenerRecall()
            self._obtenerFPR()
        
        def _obtenerFPR(self):
            self._fpr = self._fp/(self._fp+self._tn)
            
        def _obtenerPrecision(self):
            #precision = 100 * (TP / (TP+FP)) //realmente es A, de entre las veces que ha dicho A y ha acertado + las que ha fallado
            self._precision = 100 * (self._tp/(self._tp+self._fp))
            #print("Precision: " )
            #print (str(self._precision)+"%")
        
        def _obtenerRecall(self):
            #recall = TP / (TP+FN) //realmente es A de entre las veces que ha dicho que lo era y que ha dicho que no lo era cuando realmente si era
            self._recall = self._tp/(self._tp+self._fn)
            #print("Recall: ")
            #print(self._recall)        
