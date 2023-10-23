# En este código se encuentran las diferentes operaciones en espacios de vectoriales, tanto de matrices como de vectores
# Librería que se realizó para la materia CNYT de la Escuela Colombiana de Ingeniería. Durante la semana 3. Fecha: 30/08/23
# Santiago Avellaneda Rodríguez

import complexNumbersLibrary as cl
import math

# Adición de vectores complejos
def sumaVect(v1, v2):
    if len(v1)==len(v2):
        v3 = [[0] for i in range(len(v1))]
        for i in range(len(v1)):
            v3[i][0]= cl.sumCmplx(v1[i][0],v2[i][0])
        return v3
    raise Exception ("los vectores no tienen misma longitud!")

# Inverso aditivo de un vector de complejos
def invVect(v):
    for i in range(len(v)):
        v[i][0] = cl.invCmplx(v[i][0])
    return v

# Escalar por un vector
def multEscVect(esc, vect):
    for i in range(len(vect)):
        vect[i][0] = cl.multEscCmplx(esc,vect[i][0])
    return vect

# Transpuesta Vector
def transVect(v):
    vr = [0 for i in range(len(v))]
    for i in range(len(v)):
        vr[i] = v[i][0]
    return vr

# Conjugada de un vector
def conjVect(v):
    for i in range(len(v)):
        v[i][0] = cl.conjCmplx(v[i][0])
    return v

# Adjunta/daga de un vector
def adjVect(v):
    return transVect((conjVect(v)))

# Adición de matrices complejas
def sumMtrx(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = [[0 for i in range(len(m1[0]))] for j in range(len(m1))]
        for k in range(len(m1)):
            for l in range(len(m1[0])):
                m3[k][l] = cl.sumCmplx(m1[k][l],m2[k][l])
        return m3
    raise Exception("las matrices no tienen las mismas dimensiones!")

# Diferencia de matrices complejas
def difMtrx(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = [[0 for i in range(len(m1[0]))] for j in range(len(m1))]
        for k in range(len(m1)):
            for l in range(len(m1[0])):
                m3[k][l] = cl.restCmplx(m1[k][l], m2[k][l])
        return m3
    raise Exception("las matrices no tienen las mismas dimensiones!")

# Inversa aditiva de una matriz compleja
def invMtrx(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = cl.invCmplx(m[i][j])
    return m

# Multiplicación de un escalar por una matriz compleja
def multEscMtrx(esc, mtrx):
    for i in range(len(mtrx)):
        for j in range(len(mtrx[0])):
            mtrx[i][j] = cl.multEscCmplx(esc, mtrx[i][j])
    return mtrx

def multEscCmplxMtrx(esc, mtrx):
    for i in range(len(mtrx)):
        for j in range(len(mtrx[0])):
            mtrx[i][j] = cl.multiCmplx(esc, mtrx[i][j])
    return mtrx

# Transpuesta de una matriz/vector
def transMtrx(m):
    mTr = [[0 for i in range(len(m))] for i in range(len(m[0]))]
    for k in range(len(mTr)):
        for l in range(len(mTr[0])):
            mTr[k][l] = m[l][k]
    return mTr

# Conjugado de una matriz
def conjMtrx(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = cl.conjCmplx(m[i][j])
    return m

# Adjunta/Daga de una matriz
def adjMtrx(m):
    return transMtrx(conjMtrx(m))

# Imprimir daga
def printDagaVect(v):
    for i in range(len(v)):
        print(v[i])

# Imprimir un vector
def printVect(v):
    for i in range(len(v)):
        print(v[i][0])

# Imprimir una matriz
def printMtrx(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=" ")
        print()

# ----------------------------------------------------------------------------------------------------------------------
def multMtrxReal(m1, m2):
    if len(m1[0]) == len(m2):
        resultado = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    resultado[i][j] += m1[i][k] * m2[k][j]
        return resultado

def multMtrxMtrx(m1, m2):
    if len(m1[0]) == len(m2):
        m3 = [[(0, 0) for u in range(len(m2[0]))] for v in range(len(m1))]
        for a in range(len(m1)):
            for b in range(len(m2[0])):
                sum = (0, 0)
                for c in range(len(m2)):
                    add = cl.multiCmplx(m1[a][c], m2[c][b])
                    sum = cl.sumCmplx(sum, add)
                m3[a][b] = sum
        return m3

def accMtrxVect(m, v):
    if len(m[0]) == len(v):
        vr = [[(0, 0)] for u in range(len(v))]
        for i in range(len(m)):
            suma = (0, 0)
            for j in range(len(v)):
                suma = cl.sumCmplx(suma, cl.multiCmplx(m[i][j], v[j][0]))
            vr[i][0] = suma
        return vr
    raise Exception("La longitud no es compatible")

def trazaMtrx(m):
    traza = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == j:
                traza += m[i][j]
    return traza

def productoInternoMtrx(m1, m2):
    return trazaMtrx(multMtrxMtrx(adjMtrx(m1),m2))

def productInternoVector(v1, v2):
    if len(v1) == len(v2):
        v1 = conjVect(v1)
        sum = (0,0)
        for i in range(len(v1)):
            add = cl.multiCmplx(v1[i][0], v2[i][0])
            sum = cl.sumCmplx(sum, add)
        return sum

def normaVector(v):
    return round(math.sqrt(productInternoVector(v, v)[0]), 2)

def difVect(v1, v2):
    if len(v1) == len(v2):
        v3 = [[(0,0)] for i in range(len(v1))]
        for i in range(len(v1)):
            v3[i][0] = cl.restCmplx(v1[i][0], v2[i][0])
        return v3

def distanciaVectores(vect1, vect2):
    a = difVect(vect1, vect2)
    return round(math.sqrt(productInternoVector(difVect(vect1, vect2), difVect(vect1, vect2))[0]), 2)

def valorPropio(m, v1):
    if len(m[0]) == len(v1):
        v2 = multMtrxReal(m, v1)
        c = int(v2[0][0]) // int(v1[0][0])
        return c
#-----------------------------------------------------------------------------------------------------------------------
def checkHermitian(mtrx):
    return adjMtrx(mtrx) == mtrx

def checkUnitary(m1):
    ident = [[(0,0) for u in range(len(m1[0]))] for v in range(len(m1))]
    for i in range(len(ident)):
        for j in range(len(ident[0])):
            if i==j:
                ident[i][j] = (1,0)
    return multMtrxMtrx(m1, adjMtrx(m1)) == ident

def prodctTensorMtrx(m1, m2):
    m3 = [[(0,0) for u in range(len(m1[0]) * len(m2[0]))] for v in range(len(m1) * len(m2))]
    for j in range(len(m3)):
        for k in range(len(m3[0])):
            m3[j][k] = cl.multiCmplx(m1[j // len(m2)][k // len(m2[0])], m2[j % len(m2)][j % len(m2[0])])
    return m3
#-----------------------------------------------------------------------------------------------------------------------