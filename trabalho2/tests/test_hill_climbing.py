import unittest
import random
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from hill_climbing import random_restart_hill_climbing, hill_climbing_with_sideways_moves
from eight_queens import conflicts

class TestHillClimbing(unittest.TestCase):

    def test_random_restart_finds_solution(self):
        """
        Testa se o Hill Climbing com reinício aleatório encontra uma solução (0 conflitos).
        Usamos uma semente fixa para garantir a reprodutibilidade do teste.
        """
        random.seed(42)
        # Com max_restarts alto o suficiente, ele deve sempre encontrar uma solução.
        final_board, restarts = random_restart_hill_climbing(max_restarts=100)
        self.assertIsNotNone(final_board, "O algoritmo não deveria retornar um tabuleiro nulo.")
        final_conflicts = conflicts(final_board)
        self.assertEqual(final_conflicts, 0, "O Hill Climbing com reinício deveria encontrar uma solução com 0 conflitos.")
        self.assertGreater(restarts, 0, "Deveria levar pelo menos uma tentativa para encontrar a solução.")

    def test_sideways_moves_finds_solution_or_local_minimum(self):
        """
        Testa se o Hill Climbing com movimentos laterais retorna um tabuleiro válido.
        """
        random.seed(1) # Usamos uma semente diferente para testar outro cenário
        final_board, final_conflicts, _ = hill_climbing_with_sideways_moves(max_sideways_moves=100)
        self.assertIsNotNone(final_board, "O algoritmo não deveria retornar um tabuleiro nulo.")
        # O número de conflitos pode ser 0 (solução) ou > 0 (mínimo local), mas deve ser um inteiro.
        self.assertIsInstance(final_conflicts, int)


if __name__ == '__main__':
    unittest.main()