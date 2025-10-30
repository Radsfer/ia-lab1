import time
import random
import csv
import os

try:
    from hill_climbing import random_restart_hill_climbing, hill_climbing_with_sideways_moves
    from eight_queens import conflicts
except ImportError:
    print("Certifique-se de que os arquivos 'hill_climbing.py' e 'eight_queens.py' estão na mesma pasta.")
    exit()


def run_detailed_experiment(algorithm_func, num_runs, **kwargs):
    """
    Roda um experimento para um dado algoritmo, salvando os resultados de CADA execução.
    """
    all_runs_data = []

    print(f"\n--- Iniciando Experimento Detalhado: {algorithm_func.__name__} ({num_runs} execuções) ---")

    for i in range(num_runs):
        start_time = time.time()

        results = algorithm_func(**kwargs)
        final_board = results[0]

        # Extrai os "passos" de forma inteligente com base no algoritmo
        steps = 0
        if algorithm_func.__name__ == 'random_restart_hill_climbing':
            # Para este, os passos são o número de reinícios (results[1])
            steps = results[1] if len(results) > 1 else 0
        elif algorithm_func.__name__ == 'hill_climbing_with_sideways_moves':
            # Para este, os passos são os movimentos laterais (results[2])
            steps = results[2] if len(results) > 2 else 0

        end_time = time.time()

        run_time = end_time - start_time
        is_success = 1 if final_board and conflicts(final_board) == 0 else 0

        # Guarda os dados desta execução específica
        all_runs_data.append({
            "algoritmo": algorithm_func.__name__,
            "run": i + 1,
            "sucesso": is_success,
            "tempo_s": run_time,
            "passos": steps if is_success else None
        })

    print(f"Experimento com {algorithm_func.__name__} concluído.")
    return all_runs_data


def main():
    """
    Função principal para rodar todos os experimentos e salvar os resultados detalhados.
    """
    random.seed(42)
    NUM_EXECUTIONS = 100

    # Executa o experimento para Hill Climbing com Reinícios Aleatórios
    results_restart = run_detailed_experiment(
        random_restart_hill_climbing,
        NUM_EXECUTIONS,
        max_restarts=100
    )

    # Executa o experimento para Hill Climbing com Movimentos Laterais
    results_sideways = run_detailed_experiment(
        hill_climbing_with_sideways_moves,
        NUM_EXECUTIONS,
        max_sideways_moves=100
    )

    # Combina todos os resultados
    all_results = results_restart + results_sideways

    # --- Salvando os resultados detalhados em um novo arquivo CSV ---
    report_path = os.path.join(os.path.dirname(__file__), '..', 'results2.csv')
    csv_header = ['algoritmo', 'run', 'sucesso', 'tempo_s', 'passos']

    try:
        with open(report_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=csv_header)
            writer.writeheader()
            writer.writerows(all_results)
        print(f"\nResultados detalhados salvos com sucesso em: {report_path}")
    except IOError as e:
        print(f"\nErro ao salvar o arquivo CSV: {e}")


if __name__ == "__main__":
    main()