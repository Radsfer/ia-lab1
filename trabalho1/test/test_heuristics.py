# trabalho1/test/test_heuristics.py
import unittest
import math


from trabalho1.src.heuristics import h_manhattan, h_euclidiana


class TestHeuristics(unittest.TestCase):

    def test_manhattan_distance(self):
        p1 = (1, 2)
        p2 = (4, 6)
        # Distância esperada: |1 - 4| + |2 - 6| = 3 + 4 = 7
        self.assertEqual(h_manhattan(p1, p2), 7, "Distância de Manhattan incorreta")

        # Teste com o mesmo ponto
        self.assertEqual(h_manhattan(p1, p1), 0, "Distância de Manhattan para o mesmo ponto deve ser 0")

        # Teste com coordenadas negativas
        p3 = (-1, -1)
        p4 = (-4, -5)
        self.assertEqual(h_manhattan(p3, p4), 7, "Distância de Manhattan com negativos incorreta")

    def test_euclidean_distance(self):
        p1 = (1, 2)
        p2 = (4, 6)
        # Distância esperada: sqrt((4-1)^2 + (6-2)^2) = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5
        self.assertAlmostEqual(h_euclidiana(p1, p2), 5.0, "Distância Euclidiana incorreta")

        # Teste com o mesmo ponto
        self.assertAlmostEqual(h_euclidiana(p1, p1), 0.0, "Distância Euclidiana para o mesmo ponto deve ser 0")

        # Teste que resulta em valor não inteiro
        p3 = (0, 0)
        p4 = (1, 1)
        self.assertAlmostEqual(h_euclidiana(p3, p4), math.sqrt(2), "Distância Euclidiana incorreta para sqrt(2)")


if __name__ == '__main__':
    unittest.main()