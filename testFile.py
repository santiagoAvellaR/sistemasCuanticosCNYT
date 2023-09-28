import unittest
import math
import sistemaCuantico as sq

class TestSistemas(unittest.TestCase):
    def test_ProbabilidadEnPosicion(self):
        self.assertEqual(sq.probabilidadPos([[(0,3)],[(-2,0)]],0), 0.69)
        self.assertEqual(sq.probabilidadPos([[(3,-4)],[(7,2)]],0), 0.32)
    def test_Transicion(self):
        self.assertEqual(sq.probabilidadTransicion([[(1,0)],[(0,-1)]],[[(0,1)],[(1,0)]]), (0.0, -1.0))
        self.assertEqual(sq.probabilidadTransicion([[(0,1)],[(1,0)]],[[(1,0)],[(0,-1)]]), (0.0, 1.0))
if __name__ == '__main__':
    unittest.main()