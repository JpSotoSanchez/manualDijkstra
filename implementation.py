import Clases
import numpy as np

costoCamino = 0
noTerminado = True
grapho = Clases.Graph()

A = Clases.Node("A")
B = Clases.Node("B")
C = Clases.Node("C")
D = Clases.Node("D")
E = Clases.Node("E")
F = Clases.Node("F")

grapho.nodos.append(A)
grapho.nodos.append(B)
grapho.nodos.append(C)
grapho.nodos.append(D)
grapho.nodos.append(E)
grapho.nodos.append(F)

grapho.conexiones.append(Clases.agregarConexión(A, B, 2))
grapho.conexiones.append(Clases.agregarConexión(A, C, 3))
grapho.conexiones.append(Clases.agregarConexión(B, D, 2))
grapho.conexiones.append(Clases.agregarConexión(B, C, 1))
grapho.conexiones.append(Clases.agregarConexión(B, E, 2))
grapho.conexiones.append(Clases.agregarConexión(C, E, 3))
grapho.conexiones.append(Clases.agregarConexión(E, F, 2))
grapho.conexiones.append(Clases.agregarConexión(D, F, 5))

nodoInicio = A
nodoFin = F
nodosPorVisitar = grapho.nodos.copy()
nodosVisitados = []
nodoInicio.costoDeCamino = 0
sumaCaminos = 0

while(noTerminado):
    minNodo = Clases.encontrarMenorCosto(nodosPorVisitar)
    if minNodo != -1:
        nodoAEvaluar = nodosPorVisitar.pop(minNodo)
    else:
        nodoAEvaluar = nodosPorVisitar.pop()
    nodosVisitados.append(nodosPorVisitar.pop(minNodo))

    for i in range (len(nodoAEvaluar.edges)):
        pass
    
    if(nodoAEvaluar.nombre == nodoFin.nombre):
        noTerminado = False
        
