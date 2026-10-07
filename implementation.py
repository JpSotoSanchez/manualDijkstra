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
G = Clases.Node("G")
H = Clases.Node("H")

grapho.nodos.add(A)
grapho.nodos.add(B)
grapho.nodos.add(C)
grapho.nodos.add(D)
grapho.nodos.add(E)
grapho.nodos.add(F)
grapho.nodos.add(G)
grapho.nodos.add(H)

Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)

nodosPorVisitar = grapho.nodos.clone()
for nodo in nodosPorVisitar:
    nodo.conexionesSalida[1] = np.inf
    nodo.conexionesEntrada[1] = np.inf
nodosVisitados = []


nodoInicio = A
nodoFin = H
while(noTerminado):
    pass    
