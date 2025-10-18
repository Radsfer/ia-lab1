# trabalho1/src/main.py
import os
import sys
import csv
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from maze import Maze
from search import bfs, dfs, greedy_search, a_star
from heuristics import h_manhattan, h_diagonal, h_euclidiana



def plot_results(results, title, y_label, filename):
    labels = list(results.keys())
    values = list(results.values())

    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['#8ECDDD', '#F57C73', '#FAE38A', '#9BDEAC', '#D0A3D9', '#FFB347']

    bars = ax.bar(labels, values, color=colors)

    ax.set_ylabel(y_label)
    ax.set_title(title, fontsize=16)
    ax.tick_params(axis='x', labelsize=10)
    ax.set_xticklabels(labels, rotation=45, ha="right")

    for bar in bars:
        yval = bar.get_height()
        # **** ESTA É A LINHA CORRIGIDA ****
        # Trocamos '.4f' por '.4g' para formatação inteligente
        plt.text(bar.get_x() + bar.get_width() / 2.0, yval, f'{yval:.4g}', va='bottom', ha='center', fontsize=9)

    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '..', filename)
    plt.savefig(output_path)
    print(f"Gráfico '{filename}' salvo.")
    plt.close()



def main():
    maze_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'labirinto.txt')

    maze = Maze(maze_file_path)


    all_results = {}

    all_results['BFS'] = bfs(maze)
    all_results['DFS'] = dfs(maze)
    all_results['Gulosa (Manhattan)'] = greedy_search(maze, h_manhattan)
    all_results['Gulosa (Diagonal)'] = greedy_search(maze, h_diagonal)
    all_results['Gulosa (Euclidiana)'] = greedy_search(maze, h_euclidiana)

    all_results['A* (Manhattan)'] = a_star(maze, h_manhattan)
    all_results['A* (Diagonal)'] = a_star(maze, h_diagonal)
    all_results['A* (Euclidiana)'] = a_star(maze, h_euclidiana)


    valid_results = {name: res for name, res in all_results.items() if res}
    costs = {name: res['cost'] for name, res in valid_results.items()}
    nodes = {name: res['nodes_expanded'] for name, res in valid_results.items()}
    memory = {name: res['max_memory'] for name, res in valid_results.items()}
    runtimes = {name: res['runtime'] for name, res in valid_results.items()}

    plot_results(costs, 'Comparativo de Custo do Caminho', 'Custo (nº de passos)', 'grafico_custo.png')
    plot_results(nodes, 'Comparativo de Nós Expandidos', 'Número de Nós', 'grafico_nos_expandidos.png')
    plot_results(memory, 'Comparativo de Uso de Memória', 'Máximo de Nós na Memória', 'grafico_memoria.png')
    plot_results(runtimes, 'Comparativo de Tempo de Execução', 'Tempo (segundos)', 'grafico_tempo.png')

    report_path = os.path.join(os.path.dirname(__file__), '..', 'resultados.csv')

    csv_header = ['Algoritmo', 'Custo', 'Nos_Expandidos', 'Memoria_Maxima', 'Tempo_Execucao_s']

    with open(report_path, 'w', newline='') as f:
        writer = csv.writer(f)

        # Escreve o cabeçalho no arquivo
        writer.writerow(csv_header)

        # Itera sobre os resultados e escreve uma linha para cada algoritmo
        for name, result in all_results.items():
            if result:
                # Cria uma lista com os dados na ordem do cabeçalho
                row = [
                    name,
                    result['cost'],
                    result['nodes_expanded'],
                    result['max_memory'],
                    result['runtime']
                ]
                writer.writerow(row)
            else:
                # Se um algoritmo falhou, escreve N/A
                row = [name, 'N/A', 'N/A', 'N/A', 'N/A']
                writer.writerow(row)

    print(f"Relatório salvo em '{report_path}'")


if __name__ == "__main__":
    main()