""" PROGRAMA 7: Ruta más corta

Aguilar Plascencia Laura Fabiola
Flores Gomez Jessica Victoria
Martínez Martínez Yanni

Programa:
♦Implementar el algoritmo de Dijkstra para obtener la ruta más corta.
 """
class Grafo: 
    """ Clase que permite representar un grafo de forma sencilla """
    def __init__(self, nodos=[]):
        """ Constructor, permite inicializar el grafo con un conjunto de nodos """
        self.nodosEnGrafo = nodos

    def listasCostos(self):
        """ Permite tener una lista o conjunto de costos de los nodos """
        for nodo in self.nodosEnGrafo: #Recorre los nodos
            nodo.contruyeListaCostos(self) #Manda a llamar a la función que añade los costos

    def obtenerNodo(self, nombreNodo):
        """ Permite obtener el nodo en función del nombre del nodo """
        for nodo in self.nodosEnGrafo: #Recorre los elementos
            if nodo.nombreNodo == nombreNodo: #Si está en el grafo lo retorna
                return nodo

    def obtenerElementoCerca(self, nodoOrigen, nodoDestino):
        """ Permite determinar el elemento más cercano """
        nodoActual = self.obtenerNodo(nodoOrigen)
        return nodoActual.obtenerElementoMasCerca(nodoDestino)

    def agregarNodo(self, nodo):
        """ Permite agregar un nodo al conjunto de nodos del grafo """
        self.nodosEnGrafo.append(nodo)

    def agregarNodos(self, listaNodos):
        """ Permite agregar una serie de nodos al grafo """
        for nodo in listaNodos:
            self.agregarNodo(nodo)


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
        #Indica los costos que tendrá 
        self.tablaDeCostos = {self.nombreNodo: {'Costo': 0, 'Previo': None}}

        #Recorre los nodos vecinos y les asigna su respectivo costo de viaje
        for nombre, costo in self.vecinos.items():
            self.tablaDeCostos[nombre] = {'Costo': costo, 'Previo': self.nombreNodo}

    
    def obtenerElementoMasCerca(self, nombreNodo):
        """ Se encarga de la lógica para obtener el nodo más próximo """
        elementoMasCerca = []
        costos = []
        costoTotal = self.tablaDeCostos[nombreNodo]['Costo'] 
        nodoActual = nombreNodo[:]
        #Establecimos un rango en el que puede recorrer hasta 100 elementos considerando que será un programa pequeño
        for _ in range(100):
            elementoMasCerca.append(nodoActual) #El elemento más cercano lo agregamos a la lista de elementos más cercanos
            #Si aún hay elementos en los nodos
            if self.tablaDeCostos[nodoActual]['Previo'] != None:
                #Se agrega el costo y el elemento que le antecede
                costos.append(self.tablaDeCostos[nodoActual]['Costo'] - self.tablaDeCostos[self.tablaDeCostos[nodoActual]['Previo']]['Costo'])

            nodoActual = self.tablaDeCostos[nodoActual]['Previo']
            #Si ya no existen elementos entonces simplemente sale del ciclo for
            if nodoActual == None:
                break

        #Invierte la lsita de costos y la almacena en una variable para posteriormente verla
        costos = list(reversed([str(cost) for cost in costos])) 
        #Variable de resultado
        resultado = ''

        #Recorre la lista de elementos cercanos obtenidos
        for indice, tmp in enumerate(reversed(elementoMasCerca)):
            #Si aún puede recorrer entonces imprime el valor del costo y el elemento
            if indice < len(costos):
                resultado += tmp + f' > [{costos[indice]}]> '
            #Sino solo avanza
            else:
                resultado += tmp
        #Representa el costo total
        resultado += f'\nSu trayecto tuvo un costo total de : {costoTotal}'

        return resultado

    def contruyeListaCostos(self, grafo):
        """ Permite construir una lista de costos que existen en el grafo """
        visitados = [self.nombreNodo]

        #si no se establece un valor en el nodo se le pone un valor extremadamente grande para simular el infinito
        for nodo in grafo.nodosEnGrafo:
            if nodo.nombreNodo not in self.tablaDeCostos:
                #Simula el infinito del algoritmo
                self.tablaDeCostos[nodo.nombreNodo] = {'Costo': 10**10, 'Previo': None}

        #Se declara una lista de elementos que aun no han sido visitados
        novisitados = [nodo.nombreNodo for nodo in grafo.nodosEnGrafo if nodo.nombreNodo != self.nombreNodo]

        #De nueva cuenta recorre 100 veces pensando que es un programa pequeño
        for _ in range(100):
            #Se realizó una convención del ciclo for que nos devuelve una tupla capás de localizar el costo y el nombre del nodo 
            #Sobre el cual se está trabajando
            costoMinimo, nodoMinimo = min([(self.tablaDeCostos[nombreNodo]['Costo'], nombreNodo) for nombreNodo in novisitados])

            #Obteniendo el nodo con valor mínimo
            nodoMinimo = grafo.obtenerNodo(nodoMinimo)

            #Recorriendo el diccionario de elementos vecinos
            for nombreNodo, cost in nodoMinimo.vecinos.items():
                #Actualiza el valor del elemento de costo total
                distanciaFinal = costoMinimo + cost

                #Actualiza la tabla de costos
                if distanciaFinal < self.tablaDeCostos[nombreNodo]['Costo']:
                    self.tablaDeCostos[nombreNodo]['Costo'] = distanciaFinal
                    self.tablaDeCostos[nombreNodo]['Previo'] = nodoMinimo.nombreNodo

                #El nodo lo agrega a la lista de visitados para no repetir los vecinos
                visitados.append(nodoMinimo.nombreNodo)

                #Si el valor minimo está en la lista de no visitados entonces solo se remueve de la lista
                if nodoMinimo.nombreNodo in novisitados:
                    novisitados.remove(nodoMinimo.nombreNodo)
            
            if len(novisitados) == 0:
                break
        
if __name__ == '__main__':
    """ Función principal en donde se manda a llamar todas las clases, métodos y funciones """
    #Declaración de nodos:
    A = Nodo('A', {'B': 5, 'C': 7, 'D': 2})
    B = Nodo('B', {'A': 5, 'E': 4})
    C = Nodo('C', {'A': 7, 'D': 3, 'F': 5})
    D = Nodo('D', {'A': 2, 'C': 3, 'E': 4, 'G': 6})
    E = Nodo('E', {'B': 4, 'D': 4, 'G': 2})
    F = Nodo('F', {'C': 5, 'G': 7, 'H': 6 })
    G = Nodo('G', {'D': 6, 'E': 2, 'F': 7, 'H': 3})
    H = Nodo('H', {'F': 6, 'G': 3})

    #Declaración de instancia Grafo:
    grafo = Grafo()
    #Inicializar con los nodos
    grafo.agregarNodos([A, B, C, D, E, F, G, H])
    #Lista los costos de los nodos
    grafo.listasCostos()
    #indica por donde empieza y donde termina
    print(grafo.obtenerElementoCerca('A', 'H'))