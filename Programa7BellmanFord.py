""" PROGRAMA 7: BellmanFord

Aguilar Plascencia Laura Fabiola
Flores Gomez Jessica Victoria
Martínez Martínez Yanni

Programa:
♦Elegir entre el algoritmo de Bellman-Ford-Moore y A∗ para implementarl
 """
  
class Grafo: 
    """ Definiendo una estructura muy sencilla de grafo compuesto 
    por vertices y un arreglo vacio donde se almacenarán los valores
    del nodo y el valor que se tiene"""
    def __init__(self,vertices): 
        """ Constructor, permite inicializar el grafo con un arreglo vacio y
        un conjunto de vertices """
        self.vertices= vertices 
        self.grafo = []  
   
    
    def agregarVertice(self,origen,destino,peso): 
        """ Agrega un vertice en donde se le especifican valores como el nodo
        origen, el nodo destino y el peso que tiene el viaje """
        self.grafo.append([origen, destino, peso]) 
          
    
    def imprimirVertices(self, distancia): 
        """ Permite imprimir como quedó el arreglo final donde se mostrará
        el valor del vertice y la distancia que hay respecto al origen """
        #Encabezado
        print("Vertice\t\tDist. desde el origen") 
        #Recorre los vertices del grafo
        for i in range(self.vertices): 
            #Imprime la distancia que existe con respecto al origen
            print("%d \t\t %d" % (i, distancia[i])) 
      
    
    def BellmanFord(self, src): 
        """ Método que se encarga de hacer todo el proceso siguiendo el algoritmo
        visto en clase"""
        distancia = [float("Inf")] * self.vertices
        #El float("inf") hace referencia a un número infinito en python, 
        #por lo que le asignamos ese valor al vertice, es decir, inicializamos un arreglo
        #Con valores infinitos
        distancia[src] = 0 
        #Al primer indice le asignamos el valor de 0 puesto que es el origen
  
        #Recorremos todos los vertices del grafo
        for i in range(self.vertices - 1): 
            for origen, destino, peso in self.grafo: #Obteniendo una tupla al recorrer el gráfo
                #Si el peso es menor entonces que guarde ese valor en el arreglo de distancias
                if distancia[origen] != float("Inf") and distancia[origen] + peso < distancia[destino]: 
                        distancia[destino] = distancia[origen] + peso 
        #Imprimiendo las distancias
        self.imprimirVertices(distancia) 
  
grafo = Grafo(5) 

grafo.agregarVertice(0, 1, 5) 
grafo.agregarVertice(0, 2, 13) 
grafo.agregarVertice(1, 2, 24) 
grafo.agregarVertice(1, 3, 8) 
grafo.agregarVertice(1, 4, 22) 
grafo.agregarVertice(3, 2, 1) 
grafo.agregarVertice(3, 1, 3) 
grafo.agregarVertice(4, 3, 3) 

print ("Este fue el camino más corto partiendo desde el origen :D")
  
grafo.BellmanFord(0) 