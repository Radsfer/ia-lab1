# trabalho1/src/heuristics.py
from typing import Tuple

Pos = Tuple[int, int]

def h_manhattan(a: Pos, b: Pos) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def h_euclidiana(a: Pos, b: Pos) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# --- NOVA HEURÍSTICA ---
def h_diagonal(a: Pos, b: Pos) -> float:
    """Calcula a Distância Diagonal (Chebyshev)."""
    (x1, y1) = a
    (x2, y2) = b
    return max(abs(x1 - x2), abs(y1 - y2))