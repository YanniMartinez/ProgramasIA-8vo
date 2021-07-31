""" PROGRAMA 8: Modelo de Markov

Aguilar Plascencia Laura Fabiola
Flores Gomez Jessica Victoria
Martínez Martínez Yanni

Programa:
♦Desarrollar un código que reciba la gráfica que representa un modelo de Markov y genere
cadenas de forma similar a las obtenidas en el sitio mostrado en clase (http://setosa.io/ev/markov-
chains/).
 """
import random

class Grafo: 
    """ Clase que permite representar un grafo de forma sencilla """
    def __init__(self, nodos=[]):
        """ Constructor, permite inicializar el grafo con un conjunto de nodos """
        self.nodosEnGrafo = nodos

    def obtenerNodo(self, nombreNodo):
        """ Permite obtener el nodo en función del nombre del nodo """
        for nodo in self.nodosEnGrafo: #Recorre los elementos
            if nodo.nombreNodo == nombreNodo: #Si está en el grafo lo retorna
                return nodo

  
    def agregarNodo(self, nodo):
        """ Permite agregar un nodo al conjunto de nodos del grafo """
        self.nodosEnGrafo.append(nodo)

    def agregarNodos(self, listaNodos):
        """ Permite agregar una serie de nodos al grafo """
        for nodo in listaNodos:
            self.agregarNodo(nodo)
    
    def Markov (self, iteraciones ):
        """ Representa el modelo de Markov
            iteraciones hace referencia al número de pasos que hará el modelo
            Esto indicará el número de elementos

            Finalmente retorna la cadena resultante
        """
        nodoActual = 0
        contador = 0
        trayectoria = "A" #Permite desplegar el trayecto que tiene automata
        cadenaMarkov = "A" #Permite almacenar el valor final

        print(trayectoria) #Imprime el estado inicial

        #Determina las iteraciones 
        while(contador < iteraciones):
          probabilidad = (random.randrange(0,100,10))/100

          if( probabilidad <=  self.nodosEnGrafo[nodoActual].vecinos.get("A") ):
            nodoActual = 0 #Hace cambio de nodo
            trayectoria += " -> A"
            print(trayectoria)
            cadenaMarkov += "A"
          elif (probabilidad > self.nodosEnGrafo[nodoActual].vecinos.get("A")):
            nodoActual = 1 #Hace cambio de nodo
            trayectoria += " -> B"
            print(trayectoria)
            cadenaMarkov += "B"
          contador = contador +1

        return cadenaMarkov


class Nodo:
    """ Clase que permite representar de una manera muy sencilla un nodo
    Compuesto por: 
        Un nombre.
        Elementos vecinos.
        Costo de viaje
     """
    def __init__(self, nombreNodo, vecinos):
        """ Constructor del nodo, inicializa el nombre y los nodos vecinos a los
        que puede desplazarse """
        self.nombreNodo = nombreNodo
        self.vecinos = vecinos
        

if __name__ == '__main__':
    """ Función principal en donde se manda a llamar todas las clases, métodos y funciones 
        
        Declaración de nodos, el valor es la probabilidad
        de que vaya de un punto a otro, la suma debe ser  1 ó 100%:
        Importante respetar el orden de las referencias dentro de los nodos, sólo se 
        modifica la probabilidad.
    """
    A = Nodo('A', {'A': 0.5, 'B': 0.5})
    B = Nodo('B', {'A': 0.4, 'B': 0.6})
    
    #Declaración de instancia Grafo:
    grafo = Grafo()
    #Inicializar con los nodos
    grafo.agregarNodos([A, B])
    print("Su cadena mediante el método de Markov es: " + grafo.Markov(6))