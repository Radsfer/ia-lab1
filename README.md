
# Trabalhos de Inteligência Artificial - Busca em Labirinto e 8 Rainhas

Este repositório contém as implementações e análises de algoritmos de busca para a disciplina de Inteligência Artificial, divididos em dois trabalhos principais.

## Estrutura do Projeto

O projeto segue uma estrutura modular, com o código-fonte, dados e testes para cada trabalho localizados em suas respectivas pastas (`trabalho1/` e `trabalho2/`).

## Como Reproduzir os Resultados

Siga os passos abaixo para instalar as dependências e executar as análises de ambos os trabalhos.

### 1. Pré-requisitos

* Python 3.8+

### 2. Instalação das Dependências

O arquivo `requirements.txt` lista todas as bibliotecas externas necessárias para executar ambos os projetos. Para instalá-las, navegue até a pasta raiz do projeto (`ia-lab1/`) e execute o seguinte comando no seu terminal:

```bash
pip install -r requirements.txt
````

-----

## Trabalho 1: Busca em Labirinto

Este trabalho foca na implementação e análise de algoritmos de busca informada e não informada para a resolução de um problema de labirinto.

### Algoritmos Implementados

  * **Buscas Não Informadas:**
      * Busca em Largura (BFS)
      * Busca em Profundidade (DFS)
  * **Buscas Informadas (Heurísticas):**
      * Busca Gulosa (Greedy Best-First Search)
      * A\* (A-Star)

### Execução e Resultados

O script principal que executa todos os algoritmos e gera os artefatos de análise é o `main.py` do trabalho 1.

Para executá-lo, utilize o seguinte comando a partir da pasta raiz do projeto (`ia-lab1/`):

```bash
python trabalho1/src/main.py
```

Após a execução, os seguintes arquivos serão criados ou atualizados dentro da pasta `trabalho1/`:

  * `resultados.csv`: Tabela com as métricas de desempenho de cada algoritmo.
  * `grafico_custo.png`: Gráfico comparativo do custo do caminho.
  * `grafico_memoria.png`: Gráfico comparativo do uso de memória.
  * `grafico_nos_expandidos.png`: Gráfico do número de nós expandidos.
  * `grafico_tempo.png`: Gráfico comparativo do tempo de execução.

-----

## Trabalho 2: O Problema das 8 Rainhas com Hill Climbing

Este trabalho explora a resolução do problema das 8 Rainhas utilizando o algoritmo Hill Climbing e suas variações para escapar de mínimos locais.

### Algoritmos Implementados

  * Hill Climbing com Reinício Aleatório (`random_restart_hill_climbing`)
  * Hill Climbing com Movimentos Laterais (`hill_climbing_with_sideways_moves`)

### Execução dos Experimentos

O script `main.py` do trabalho 2 executa 100 vezes cada variação do Hill Climbing para coletar dados de desempenho.

Para executá-lo, utilize o seguinte comando a partir da pasta raiz (`ia-lab1/`):

```bash
python trabalho2/src/main.py
```

A execução irá gerar o arquivo `results2.csv` na pasta `trabalho2/`, contendo os dados brutos de cada uma das 200 execuções.

### Análise dos Resultados

Para processar os dados e gerar a análise estatística e os gráficos comparativos, execute o script de análise:

```bash
python trabalho2/tests/analysis.py
```

Este script irá ler o arquivo `results2.csv` e gerar os seguintes artefatos na pasta `trabalho2/`:

  * **Saída no console:** Uma tabela com a análise estatística detalhada.
  * `boxplot_tempo.png`: Gráfico com a distribuição do tempo de execução.
  * `boxplot_passos.png`: Gráfico com a distribuição do número de passos (reinícios ou movimentos laterais).
  * `taxa_sucesso.png`: Gráfico de barras comparando a taxa de sucesso de cada algoritmo.


