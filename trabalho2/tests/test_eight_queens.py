import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from eight_queens import initial_board, conflicts, neighbors, N

class TestEightQueens(unittest.TestCase):

    def test_initial_board_creation(self):
        """Testa se o tabuleiro inicial é criado com o tamanho correto."""
        board = initial_board()
        self.assertEqual(len(board), N, "O tabuleiro deve ter N colunas.")
        for row in board:
            self.assertTrue(0 <= row < N, "Cada rainha deve estar em uma linha válida.")

    def test_conflicts_on_known_solution(self):
        """Testa se uma solução conhecida tem 0 conflitos."""
        solution_board = [4, 2, 0, 6, 1, 7, 5, 3]
        self.assertEqual(conflicts(solution_board), 0, "Uma solução válida não deve ter conflitos.")

    def test_conflicts_on_diagonal(self):
        """Testa se um tabuleiro com todas as rainhas na diagonal principal tem o número correto de conflitos."""
        # Em uma diagonal, cada rainha ataca todas as outras.
        # O número de pares é N * (N - 1) / 2
        # Para N=8, são 8 * 7 / 2 = 28 conflitos.
        diagonal_board = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(conflicts(diagonal_board), 28, "Conflitos na diagonal principal calculados incorretamente.")

    def test_conflicts_on_same_row(self):
        """Testa se um tabuleiro com todas as rainhas na mesma linha tem o número correto de conflitos."""
        # Mesma lógica da diagonal: 28 conflitos.
        same_row_board = [0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(conflicts(same_row_board), 28, "Conflitos na mesma linha calculados incorretamente.")

    def test_neighbors_count(self):
        """Testa se a função de vizinhança gera o número correto de vizinhos."""
        # Para cada uma das 8 colunas, podemos mover a rainha para 7 outras linhas.
        # Total de vizinhos = 8 * 7 = 56.
        board = initial_board()
        neighbor_list = list(neighbors(board))
        self.assertEqual(len(neighbor_list), N * (N - 1), "Número incorreto de vizinhos gerados.")

if __name__ == '__main__':
    unittest.main()