# Trabalho 1 - Busca em Labirinto (Inteligência Artificial)

Este repositório contém a implementação e análise de algoritmos de busca informada e não informada para a resolução de um problema de labirinto, conforme especificado na disciplina de Inteligência Artificial.

## Estrutura do Projeto

O projeto segue a estrutura recomendada, com o código-fonte localizado em `trabalho1/src/`, os dados do labirinto em `trabalho1/data/`, e os testes unitários em `trabalho1/test/`.

## Algoritmos Implementados

* **Buscas Não Informadas:**
    * Busca em Largura (BFS)
    * Busca em Profundidade (DFS)
* **Buscas Informadas (Heurísticas):**
    * Busca Gulosa (Greedy Best-First Search)
    * A* (A-Star)

As buscas informadas foram avaliadas com as heurísticas de Distância de Manhattan, Diagonal e Euclidiana para uma análise comparativa completa.

## Como Reproduzir os Resultados

Siga os passos abaixo para instalar as dependências e executar a análise para gerar os resultados.

### 1. Pré-requisitos

* Python 3.8+

### 2. Instalação das Dependências

O arquivo `requirements.txt` lista as bibliotecas externas necessárias para executar o projeto. Para instalá-las, navegue até a pasta raiz do projeto (`ia-lab1/`) e execute o seguinte comando no seu terminal:

```bash
pip install -r requirements.txt
```

### 3. Execução

O script principal que executa todos os algoritmos e gera os artefatos de análise é o `main.py`.

Para executá-lo, utilize o seguinte comando a partir da pasta raiz do projeto (`ia-lab1/`):

```bash
python trabalho1/src/main.py
```

### 4. Resultados Gerados

Após a execução do script, os seguintes arquivos serão criados ou atualizados dentro da pasta `trabalho1/`, contendo todos os dados para a análise do relatório:

* `resultados.csv`: Uma tabela com as métricas de desempenho de cada algoritmo.
* `grafico_custo.png`: Gráfico comparativo do custo (comprimento) do caminho encontrado.
* `grafico_memoria.png`: Gráfico comparativo do uso máximo de memória.
* `grafico_nos_expandidos.png`: Gráfico comparativo do número de nós expandidos.
* `grafico_tempo.png`: Gráfico comparativo do tempo de execução.
* `grafico_tempo.png`: Gráfico comparativo do tempo de execução.