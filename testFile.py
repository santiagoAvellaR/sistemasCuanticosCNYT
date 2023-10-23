# En este código se encuentran las diferentes pruebas realizadas para comprobar el buen funcionamiento de las funciones que se crearon
# en el archivo matrxVectorsLibrary.py
import unittest
import math
import sistemaCuantico as sc

class TestQuantumSystems(unittest.TestCase):
    def test_ModVector(self):
        self.assertEqual(sc.modVect([[(1,0)],[(1,0)]]), 1.4142135623730951)
        self.assertEqual(sc.modVect([[(1, 0)], [(1, 0)],[(1,0)],[(2,0)],[(3,0)]]), 4)

    def test_normalizeVector(self):
        self.assertEqual(sc.normalizeVector([[(1,0)],[(1,0)]]), [[(0.7071067811865475, 0.0)], [(0.7071067811865475, 0.0)]])
        self.assertEqual(sc.normalizeVector([[(1, 0)], [(1, 0)],[(1,0)],[(2,0)],[(3,0)]]), [[(0.25, 0.0)], [(0.25, 0.0)], [(0.25, 0.0)], [(0.5, 0.0)], [(0.75, 0.0)]])

    def test_probabilityPosition(self):
        self.assertEqual(sc.probabilidadPos([[(0,3)],[(-2,0)]],0), 0.69)
        self.assertEqual(sc.probabilidadPos([[(3,-4)],[(7,2)]],0), 0.32)

    def test_transitionAmplitud(self):
        self.assertEqual(sc.probabilidadTransicion([[(1,0)],[(0,-1)]],[[(0,1)],[(1,0)]]), (0.0, -1.0))
        self.assertEqual(sc.probabilidadTransicion([[(0,1)],[(1,0)]],[[(1,0)],[(0,-1)]]), (0.0, 1.0))

    def test_expectedValue(self):
        self.assertEqual(sc.valorEsperado([[(1,0),(0,1)],[(0,-1),(2,0)]], [[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]),(2.5, 0.0))
        self.assertEqual(sc.valorEsperado([[(1,0),(0,-1)],[(0,1),(2,0)]], [[(math.sqrt(2)/2,0)],[(0,math.sqrt(2)/2)]]), (0.49, 0.0))

    def test_variance(self):
        self.assertEqual(sc.variance([[(1,0),(0,1)],[(0,-1),(2,0)]], [[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]), (0.25, 0.0))
        self.assertEqual(sc.variance([[(1,0),(0,-1)],[(0,1),(2,0)]], [[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]), (0.26, 0.0))

    def test_probabilityAfterObservation(self):
        self.assertEqual(sc.probabilidadObservacion([[(1,0),(0,1)],[(0,-1),(2,0)]], [[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]), 0.49)
        self.assertEqual(sc.probabilidadObservacion([[(1,0),(0,-1)],[(0,1),(2,0)]], [[((2**0.5)/2,0)],[(0,(2**0.5)/2)]]), 0.96)

if __name__ == '__main__':
    unittest.main()