import unittest
import os

from trabalho1.src.maze import Maze

class TestMaze(unittest.TestCase):

    def setUp(self):
        self.test_maze_file = 'trabalho1/tests/test_labirinto.txt'
        os.makedirs(os.path.dirname(self.test_maze_file), exist_ok=True)

        with open(self.test_maze_file, 'w') as f:
            f.write("S.G\n")
            f.write(".#.\n")
            f.write("...\n")

        self.maze = Maze(self.test_maze_file)

    def tearDown(self):
        os.remove(self.test_maze_file)

    def test_carregamento_labirinto(self):
        self.assertEqual(self.maze.H, 3)
        self.assertEqual(self.maze.W, 3)
        self.assertEqual(self.maze.start, (0, 0))
        self.assertEqual(self.maze.goal, (0, 2))

    def test_in_bounds(self):
        self.assertTrue(self.maze.in_bounds((0, 0)))
        self.assertFalse(self.maze.in_bounds((-1, 0)))

    def test_is_passable(self):
        self.assertTrue(self.maze.is_passable((0, 1)))
        self.assertFalse(self.maze.is_passable((1, 1)))

    def test_goal_test(self):
        self.assertTrue(self.maze.goal_test((0, 2)))
        self.assertFalse(self.maze.goal_test((0, 0)))

    def test_get_neighbors(self):
        neighbors_start = self.maze.get_neighbors((0, 0))
        self.assertCountEqual(neighbors_start, [(1, 0), (0, 1)], "Vizinhos de (0,0) incorretos")

        neighbors_middle = self.maze.get_neighbors((2, 1))
        self.assertCountEqual(neighbors_middle, [(2, 0), (2, 2)], "Vizinhos de (2,1) incorretos")

        neighbors_near_wall = self.maze.get_neighbors((1, 0))
        self.assertCountEqual(neighbors_near_wall, [(0, 0), (2, 0)], "Vizinhos de (1,0) incorretos")


if __name__ == '__main__':
    unittest.main()