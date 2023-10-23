# Santiago Avellaneda Rodríguez - CNYT 2023-2
import complexNumbersLibrary as cnl
import matrxVectorsLibrary as mvl
import math
import numpy as np
import matplotlib.pyplot as plt


# Crear una matriz identidad de tamaño "tam"
def createIdentity(tam):
    iden = [[(0,0) for u in range(tam)] for v in range(tam)]
    for i in range(tam):
        for j in range(tam):
            if i == j:
                iden[i][j] = (1,0)
    return iden

# Hallar el modulo de un vector
def modVect(vector):
    mod = 0
    for i in range(len(vector)):
        mod += pow(cnl.modCmplx(vector[i][0]),2)
    return math.sqrt(mod)

# Normalizar un vector
def normalizeVector(vector):
    modVector = modVect(vector)
    for i in range(len(vector)):
        vector[i][0] = (vector[i][0][0] / modVector, vector[i][0][1] / modVector)
    return vector

# Probabilidad por posicion
def probabilidadPos(vect, pos):
    if modVect(vect) != 1:
        vect = normalizeVector(vect)
    return round(pow(cnl.modCmplx(vect[pos][0]), 2),2)

#  Probabilidad de transicion
def probabilidadTransicion(vectorIni, vectorFin):
    if modVect(vectorIni) != 1:
        vectorIni = normalizeVector(vectorIni)
    if modVect(vectorFin) != 1:
        vectorFin = normalizeVector(vectorFin)
    return mvl.productInternoVector(vectorFin, vectorIni)

# Valor esperado
def valorEsperado(matriz, ket):
    if not mvl.checkHermitian(matriz):
        return mvl.productInternoVector(mvl.accMtrxVect(matriz, ket), ket)
    else:
        raise Exception ("La matriz no es hermitiana")

# Varianza / media
def variance(matrix, kett):
    if not mvl.checkHermitian(matrix):
        val = valorEsperado(matrix, kett)
        dif = mvl.difMtrx(matrix, mvl.multEscCmplxMtrx(val, createIdentity(len(matrix))))
        delta = mvl.multMtrxMtrx(dif, dif)
        return mvl.productInternoVector(mvl.accMtrxVect(delta, kett), kett)
    raise Exception("La matriz no es hermitiana")

# Valores propios
def valoresPropios(matrix):
    matrix = np.array(matrix)
    vals = np.linalg.eigvals(matrix)
    return vals

# Vectores propios
def vectoresPropios(matrix):
    matrix = np.array(matrix)
    vals, vects = np.linalg.eig(matrix)
    return vects

# Probabilidad tras una observacion
def probabilidadObservacion(matriz, ket):
    return round(math.pow(cnl.modCmplx(probabilidadTransicion(ket, mvl.accMtrxVect(matriz, ket))), 2), 2)

# Dinamica en sistemas
def marbleSimulation(Dynamics, iniState, clicks, numb):
    finState = iniState
    for i in range(clicks):
        finState = mvl.accMtrxVect(Dynamics, finState)
    categorias = [str(j) for j in range(len(iniState))]
    valores = [0 for i in range(len(finState))]
    for i in range(len(finState)):
        valores[i] = finState[i][0][0]
    fig, ax = plt.subplots()
    ax.bar(categorias, valores)
    ax.set_xlabel('Cajas')
    ax.set_ylabel('Canicas')
    ax.set_title('Marble Simulation ' + str(numb))
    plt.savefig('graficoMarbleSimulation' + str(numb) + '.png')
    plt.show()
    return finState

# Simulador de sistemas lineales
def dinamicaSistemaLineal(vect, numMatrices):
    almacen = [[] for a in range(numMatrices)]
    for pos in range(numMatrices):
        almacen[pos] = input("Introduzca la matriz")
    ini = vect
    index = len(almacen)-1
    while index != 0:
        ini = mvl.accMtrxVect(almacen[index], ini)
    return ini

#-----------------------------------------------------------------------------------------------------------------------
# EJERCICIOS
# 4.3.1.
def ex431():
    # Se va a evitar el uso de la constante de Planck Reducida ya que este es un número muy pequeño y python a veces no los reconoce
    # o los redondea por defecto
    sx = [[(0,0),(1, 0)],[(1, 0),(0,0)]]
    ini = [[(1,0)], [(0,0)]]
    print(mvl.accMtrxVect(sx, ini))
    # La probabilidad que se encuentre en spin Up es de cero, ya que al actuar con sx, si o si va a cambiar de estado a spin down

# 4.3.2
def ex432():
    # Se va a evitar el uso de la constante de Planck Reducida ya que este es un número muy pequeño y python a veces no los reconoce
    # o los redondea por defecto
    sx = [[(0,0),(1, 0)],[(1, 0),(0,0)]]
    ini = [[(1,0)], [(0,0)]]
    v1 = [[(-1,0)],[(1,0)]]
    v2 = [[(1,0)],[(1,0)]]
    print(probabilidadTransicion(ini, v1))
    print(probabilidadTransicion(ini, v2))

# 4.4.1
def ex441():
    mat1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
    mat2 = [[(math.sqrt(2)/2, 0), (math.sqrt(2)/2, 0)],[(math.sqrt(2)/2, 0),(-math.sqrt(2)/2, 0)]]
    print(mvl.checkUnitary(mat1))
    print(mvl.checkUnitary(mat2))
    print(mvl.checkUnitary(mvl.multMtrxMtrx(mat1, mat2)))

# 4.4.2
def ex442():
    dinamica = [[(0, 0), (1/(2*(1/2)), 0), (1/(2*(1/2)), 0), (0, 0)],
                        [(0,1/(2*(1/2))), (0, 0), (0, 0), (1/(2*(1/2)), 0)],
                        [(1 / (2 * (1 / 2)), 0), (0, 0), (0, 0), (0,1 / (2 * (1 / 2)))],
                        [(0, 0), (1/(2*(1/2)), 0), (-1/(2*(1/2)), 0), (0, 0)]]
    print(marbleSimulation(dinamica, [[(1,0)],[(0,0)],[(0,0)],[(0,0)]],3,1))

def casosPrueba2():
    print(probabilidadPos([[(0,3)],[(-2,0)]],0))
    print(probabilidadPos([[(3,-4)],[(7,2)]],0))
    print()
    print(probabilidadTransicion([[(1,0)],[(0,-1)]],[[(0,1)],[(1,0)]]))
    print(probabilidadTransicion([[(0,1)],[(1,0)]],[[(1,0)],[(0,-1)]]))
    print()
    print(modVect([[(1,0)],[(1,0)]]))
    print(modVect([[(1, 0)], [(1, 0)],[(1,0)],[(2,0)],[(3,0)]]))
    print()
    print(normalizeVector([[(1,0)],[(1,0)]]))
    print(normalizeVector([[(1, 0)], [(1, 0)],[(1,0)],[(2,0)],[(3,0)]]))
    print()
    print(valorEsperado([[(1,0),(0,1)],[(0,-1),(2,0)]], [[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]))
    print(valorEsperado([[(1,0),(0,-1)],[(0,1),(2,0)]], [[(math.sqrt(2)/2,0)],[(0,math.sqrt(2)/2)]]))
    print()
    print(variance([[(1,0),(0,1)],[(0,-1),(2,0)]], [[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]))
    print(variance([[(1,0),(0,-1)],[(0,1),(2,0)]], [[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]))
    print()
    print(probabilidadObservacion([[(1,0),(0,1)],[(0,-1),(2,0)]], [[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]))
    print(probabilidadObservacion([[(1,0),(0,-1)],[(0,1),(2,0)]], [[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]))