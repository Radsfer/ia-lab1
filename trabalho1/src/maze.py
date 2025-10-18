from typing import List, Tuple

Pos = Tuple[int, int]
Grid = List[List[str]]


class Maze:
    def __init__(self, filename: str):
        with open(filename, 'r') as f:
            lines = f.read().splitlines()

        # Substitui os espaços por '.' para consistência
        self.grid = [list(line.replace(' ', '')) for line in lines]
        self.H = len(self.grid)
        self.W = len(self.grid[0]) if self.H > 0 else 0

        try:
            self.start = self._find('S')
            self.goal = self._find('G')
        except ValueError as e:
            print(e)
            exit(1)

    def _find(self, char: str) -> Pos:
        for r in range(self.H):
            for c in range(self.W):
                if self.grid[r][c] == char:
                    return (r, c)
        raise ValueError(f"Caractere '{char}' não encontrado no grid.")

    def in_bounds(self, p: Pos) -> bool:
        r, c = p
        return 0 <= r < self.H and 0 <= c < self.W

    def is_passable(self, p: Pos) -> bool:
        r, c = p
        return self.grid[r][c] != '#'

    def get_neighbors(self, p: Pos) -> List[Pos]:
        r, c = p
        # Candidatos: Norte, Sul, Oeste, Leste
        candidates = [
            ('N', (r - 1, c)),
            ('S', (r + 1, c)),
            ('O', (r, c - 1)),
            ('L', (r, c + 1)),
        ]
        neighbors = []
        for action, (nr, nc) in candidates:
            neighbor_pos = (nr, nc)
            if self.in_bounds(neighbor_pos) and self.is_passable(neighbor_pos):
                neighbors.append(neighbor_pos)
        return neighbors

    def goal_test(self, p: Pos) -> bool:
        return p == self.goal

    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)