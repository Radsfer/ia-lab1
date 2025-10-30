import random
from typing import List, Iterable, Tuple

# Representação do tabuleiro: uma lista onde o índice é a coluna e o valor é a linha.
Board = List[int]
N = 8


def initial_board() -> Board:
    """
    Cria um tabuleiro inicial aleatório.
    Para cada coluna, sorteia uma linha para a rainha.
    """
    # Gera uma lista de 8 números, onde cada número (linha) é sorteado
    # aleatoriamente de 0 a 7.
    return [random.randint(0, N - 1) for _ in range(N)]


def conflicts(board: Board) -> int:
    """
    Calcula o número de pares de rainhas em conflito.
    """
    count = 0
    # Itera por cada rainha (coluna i)
    for i in range(N):
        # Compara com cada outra rainha à sua direita (coluna j)
        # para evitar contar o mesmo par duas vezes.
        for j in range(i + 1, N):
            # 1. Conflito na mesma linha
            if board[i] == board[j]:
                count += 1
            # 2. Conflito na diagonal
            # A diferença absoluta das colunas (j - i) é igual à
            # diferença absoluta das linhas.
            elif abs(board[i] - board[j]) == (j - i):
                count += 1
    return count


def neighbors(board: Board) -> Iterable[Board]:
    """
    Gera todos os tabuleiros vizinhos a partir do estado atual.
    Um vizinho é formado movendo uma rainha para uma nova linha na mesma coluna.
    """
    # Para cada coluna do tabuleiro
    for col in range(N):
        # Para cada possível nova linha nessa coluna
        for row in range(N):
            # Se a nova linha for diferente da linha atual da rainha
            if board[col] != row:
                # Cria uma cópia do tabuleiro
                new_board = board.copy()
                # Move a rainha para a nova linha
                new_board[col] = row
                # Retorna o novo tabuleiro. 'yield' é usado para retornar um
                # gerador, que é mais eficiente em memória do que criar uma
                # lista com todos os 56 vizinhos de uma vez.
                yield new_board


def display(board: Board):
    """
    Função auxiliar para imprimir o tabuleiro de forma visual.
    """
    for row in range(N):
        line = ""
        for col in range(N):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("-" * (2 * N))