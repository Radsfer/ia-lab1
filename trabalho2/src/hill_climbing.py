import random
from eight_queens import Board, conflicts, neighbors, initial_board, display


def hill_climbing_basic():
    """
    Executa o algoritmo Hill Climbing padrão a partir de um único estado inicial.
    Retorna o tabuleiro final e o número de conflitos.
    """
    current_board = initial_board()
    current_conflicts = conflicts(current_board)

    while True:
        # Encontra o melhor vizinho
        best_neighbor = None
        min_neighbor_conflicts = current_conflicts

        # Itera sobre todos os vizinhos para encontrar o melhor
        for neighbor in neighbors(current_board):
            neighbor_conflicts = conflicts(neighbor)
            if neighbor_conflicts < min_neighbor_conflicts:
                best_neighbor = neighbor
                min_neighbor_conflicts = neighbor_conflicts

        # Se nenhum vizinho for melhor, chegamos a um mínimo local
        if best_neighbor is None:
            return current_board, current_conflicts  # Retorna o tabuleiro "preso"

        # Caso contrário, move-se para o melhor vizinho
        current_board = best_neighbor
        current_conflicts = min_neighbor_conflicts

        # Se encontrarmos a solução
        if current_conflicts == 0:
            return current_board, 0


def random_restart_hill_climbing(max_restarts: int = 100):
    """
    Executa o Hill Climbing com reinícios aleatórios.
    """
    print(f"Iniciando Hill Climbing com até {max_restarts} reinícios aleatórios...")

    for i in range(max_restarts):
        # Cada reinício começa uma nova busca a partir de um tabuleiro aleatório
        # A função hill_climbing_basic fará a "subida da encosta"
        final_board, final_conflicts = hill_climbing_basic()

        # Verifica se a busca encontrou a solução (0 conflitos)
        if final_conflicts == 0:
            print(f"\nSolução encontrada após {i + 1} tentativas (reinícios)!")
            return final_board, i + 1
        else:
            # Imprime o progresso a cada 10 tentativas
            if (i + 1) % 10 == 0:
                print(f"Tentativa {i + 1}/{max_restarts}... (preso com {final_conflicts} conflitos)")

    print(f"\nNenhuma solução encontrada após {max_restarts} reinícios.")
    return None, max_restarts




def hill_climbing_with_sideways_moves(max_sideways_moves: int = 100):
    """
    Executa o Hill Climbing permitindo um número limitado de movimentos laterais (VERSÃO COM CORREÇÃO FINAL).
    """
    current_board = initial_board()
    current_conflicts = conflicts(current_board)
    sideways_moves_count = 0

    # Limite de iterações para evitar loops infinitos em platôs muito grandes.
    max_iterations = 2000
    for _ in range(max_iterations):

        # Se a solução for encontrada, retorna o resultado.
        if current_conflicts == 0:
            return current_board, 0, sideways_moves_count

        # 1. Avalia todos os vizinhos
        successors = list(neighbors(current_board))
        min_neighbor_conflicts = min(conflicts(s) for s in successors)

        # 2. Decide a ação a ser tomada

        # Caso A: Encontrou um vizinho melhor (melhora)
        if min_neighbor_conflicts < current_conflicts:
            best_successors = [s for s in successors if conflicts(s) == min_neighbor_conflicts]
            current_board = random.choice(best_successors)
            current_conflicts = min_neighbor_conflicts
            # A LINHA problematica "sideways_moves_count = 0" foi removida daqui.

        # Caso B: O melhor vizinho é um movimento lateral (empate)
        elif min_neighbor_conflicts == current_conflicts and sideways_moves_count < max_sideways_moves:
            sideways_candidates = [s for s in successors if conflicts(s) == current_conflicts]
            if sideways_candidates:
                current_board = random.choice(sideways_candidates)
                sideways_moves_count += 1 # Incrementa o contador

        # Caso C: Preso em um mínimo local (sem melhora e sem permissão para mover de lado)
        else:
            return current_board, current_conflicts, sideways_moves_count

    # Retorna o último estado se atingir o limite de iterações (timeout)
    return current_board, current_conflicts, sideways_moves_count