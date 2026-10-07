class Graph:
    nodos = []

    def __init__(self):
        pass
class Node: 
    nombre = ""
    #Son los nodos a los que se llega desde este nodo, debeguardar el nodo de conexión y el costo
    conexionesSalida = []
    #Son los nodos que llegan a este nodo, se debe guardar el nodo de conexión y el costo
    conexionesEntrada = []

    def __init__(self, nombre):
        self.nombre = nombre

    

def busquedaCamino(nodoEntrada):
    nodoEntrada

def agregarConexión(nodoEntrada, nodoLlegada, costo):
    nodoEntrada.conexionesSalida.add([nodoLlegada, costo])
    nodoLlegada.consexionesEntrada.add([nodoEntrada, costo])
