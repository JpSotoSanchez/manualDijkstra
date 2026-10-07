import Clases


costoCamino = 0
noTerminado = True

nodosVisitados = []
nodosPorVisitar = []

A = Clases.Node("A")
B = Clases.Node("B")
C = Clases.Node("C")
D = Clases.Node("D")
E = Clases.Node("E")
F = Clases.Node("F")
G = Clases.Node("G")
H = Clases.Node("H")

nodosPorVisitar.add(A)
nodosPorVisitar.add(B)
nodosPorVisitar.add(C)
nodosPorVisitar.add(D)
nodosPorVisitar.add(E)
nodosPorVisitar.add(F)
nodosPorVisitar.add(G)
nodosPorVisitar.add(H)

Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)
Clases.agregarConexión(A, B, 2)


nodoInicio = A
nodoFin = H
while(noTerminado):
    pass
