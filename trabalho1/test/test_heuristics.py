import unittest
import math
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from trabalho1.src.heuristics import h_manhattan, h_euclidiana, h_diagonal


class TestHeuristics(unittest.TestCase):

    def test_manhattan_distance(self):
        """Testa o cálculo da distância de Manhattan."""
        p1 = (1, 2)
        p2 = (4, 6)
        self.assertEqual(h_manhattan(p1, p2), 7, "Distância de Manhattan incorreta")
        self.assertEqual(h_manhattan(p1, p1), 0, "Distância de Manhattan para o mesmo ponto deve ser 0")
        p3 = (-1, -1)
        p4 = (-4, -5)
        self.assertEqual(h_manhattan(p3, p4), 7, "Distância de Manhattan com negativos incorreta")

    def test_euclidean_distance(self):
        """Testa o cálculo da distância Euclidiana."""
        p1 = (1, 2)
        p2 = (4, 6)
        self.assertAlmostEqual(h_euclidiana(p1, p2), 5.0, "Distância Euclidiana incorreta")
        self.assertAlmostEqual(h_euclidiana(p1, p1), 0.0, "Distância Euclidiana para o mesmo ponto deve ser 0")
        p3 = (0, 0)
        p4 = (1, 1)
        self.assertAlmostEqual(h_euclidiana(p3, p4), math.sqrt(2), "Distância Euclidiana incorreta para sqrt(2)")

    # --- NOVO TESTE ADICIONADO ---
    def test_diagonal_distance(self):
        """Testa o cálculo da distância Diagonal (Chebyshev)."""
        p1 = (1, 2)
        p2 = (5, 8)
        # Distância esperada: max(|1 - 5|, |2 - 8|) = max(4, 6) = 6
        self.assertEqual(h_diagonal(p1, p2), 6, "Distância Diagonal incorreta")

        # Teste com o mesmo ponto
        self.assertEqual(h_diagonal(p1, p1), 0, "Distância Diagonal para o mesmo ponto deve ser 0")

        # Teste com coordenadas negativas
        p3 = (-2, -3)
        p4 = (-7, 1)
        # Distância esperada: max(|-2 - -7|, |-3 - 1|) = max(5, 4) = 5
        self.assertEqual(h_diagonal(p3, p4), 5, "Distância Diagonal com negativos incorreta")


if __name__ == '__main__':
    unittest.main()