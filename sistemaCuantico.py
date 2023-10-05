import complexNumbersLibrary as cnl
import matrxVectorsLibrary as mvl
import math
def modVect(vector):
    mod = 0
    for i in range(len(vector)):
        mod += pow(cnl.modCmplx(vector[i][0]),2)
    return math.sqrt(mod)

def normalizeVector(vector):
    modVector = modVect(vector)
    for i in range(len(vector)):
        vector[i][0] = (vector[i][0][0] / modVector, vector[i][0][1] / modVector)
    return vector

def probabilidadPos(vect, pos):
    if modVect(vect) != 1:
        vect = normalizeVector(vect)
    return round(pow(cnl.modCmplx(vect[pos][0]), 2),2)

def probabilidadTransicion(vectorIni, vectorFin):
    if modVect(vectorIni) != 1:
        vectorIni = normalizeVector(vectorIni)
    if modVect(vectorFin) != 1:
        vectorFin = normalizeVector(vectorFin)
    return mvl.productInternoVector(vectorFin, vectorIni)

def valorEsperado(matriz, ket):
    if not mvl.checkHermitian(matriz):
        print(mvl.accMtrxVect(matriz, ket))
        return mvl.productInternoVector(mvl.accMtrxVect(matriz, ket), ket)
    else: raise Exception ("La matriz no es hermitiana")


def casosPrueba():
    print(probabilidadPos([[(0,3)],[(-2,0)]],0))
    print(probabilidadPos([[(3,-4)],[(7,2)]],0))
    print(probabilidadTransicion([[(1,0)],[(0,-1)]],[[(0,1)],[(1,0)]]))
    print(probabilidadTransicion([[(0,1)],[(1,0)]],[[(1,0)],[(0,-1)]]))

def casosPrueba2():
    print(valorEsperado([[(1,0),(0,-1)],[(0,1),(2,0)]],[[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]))
casosPrueba2()
