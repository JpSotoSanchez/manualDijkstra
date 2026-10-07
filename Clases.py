import numpy as np

class Graph:
    nodos = []
    conexiones = []

    def __init__(self):
        pass
class Node: 
    nombre = ""
    costoDeCamino = np.inf
    edges = []
    vieneDe = any
    
    def __init__(self, nombre):
        self.nombre = nombre

class Edge:
    nodoPrimero = any
    nodoSegundo = any
    peso = 0

    def __init__(self, nodo1, nodo2, costo):
        self.nodoPrimero = nodo1
        self.nodoSegundo = nodo2
        self.peso = costo
    

def agregarConexión(nodoEntrada, nodoLlegada, costo):
    edge = Edge(nodoEntrada, nodoLlegada, costo)
    nodoEntrada.edges.append(edge)
    nodoLlegada.edges.append(edge)
    return edge

def encontrarMenorCosto(lista):
    min = np.inf + 1.0
    nodo = -1
    for i in range (0, len(lista)):
        if lista[i].costoDeCamino < min:
            nodo = i
            min = lista[i].costoDeCamino
    return nodo

def actualizarCostos(edge, sumaActual):
    edge.nodoPrimero.costoDeCamino = edge.peso + sumaActual
    edge.nodoSegundo.costoDeCamino = edge.peso + sumaActual