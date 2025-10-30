import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    df = pd.read_csv('../results2.csv')
except FileNotFoundError:
    print("Erro: Arquivo 'resultados_detalhados_trabalho2.csv' não encontrado.")
    print("Certifique-se de que este script está na mesma pasta que o arquivo CSV.")
    exit()

# Mapear nomes de algoritmos para serem mais amigáveis nos gráficos
df['algoritmo'] = df['algoritmo'].replace({
    'random_restart_hill_climbing': 'Reinício Aleatório',
    'hill_climbing_with_sideways_moves': 'Movimentos Laterais'
})

# Separar os dados por algoritmo
algoritmos = df['algoritmo'].unique()
stats_list = []

for algo in algoritmos:
    df_algo = df[df['algoritmo'] == algo]
    sucesso_df = df_algo[df_algo['sucesso'] == 1]

    # Calcular estatísticas
    total_runs = len(df_algo)
    success_count = len(sucesso_df)
    failure_count = total_runs - success_count
    success_rate = (success_count / total_runs) * 100 if total_runs > 0 else 0

    # Tempo em milissegundos para facilitar a leitura
    tempo_ms_mean = sucesso_df['tempo_s'].mean() * 1000
    tempo_ms_std = sucesso_df['tempo_s'].std() * 1000

    passos_mean = sucesso_df['passos'].mean()
    passos_std = sucesso_df['passos'].std()

    # Soluções "sortudas" (passos = 0)
    lucky_shots = len(sucesso_df[sucesso_df['passos'] == 0])

    stats_list.append({
        'Algoritmo': algo,
        'Taxa de Sucesso (%)': f"{success_rate:.1f}",
        'Falhas': failure_count,
        'Tempo Médio (ms)': f"{tempo_ms_mean:.2f}",
        'Desvio Padrão (Tempo)': f"{tempo_ms_std:.2f}",
        'Passos Médios': f"{passos_mean:.2f}",
        'Desvio Padrão (Passos)': f"{passos_std:.2f}",
        'Soluções Sortudas': lucky_shots,
    })

# Criar um DataFrame com as estatísticas e imprimi-lo
stats_df = pd.DataFrame(stats_list)
print("--- Tabela de Análise Estatística ---")
print(stats_df.to_string(index=False))

# --- GERAÇÃO DE GRÁFICOS ---
sns.set_theme(style="whitegrid")

# 1. Boxplot do Tempo de Execução (em ms)
df_sucesso = df[df['sucesso'] == 1].copy()
df_sucesso['tempo_ms'] = df_sucesso['tempo_s'] * 1000

plt.figure(figsize=(10, 6))
sns.boxplot(x='algoritmo', y='tempo_ms', data=df_sucesso, palette="pastel")
plt.title('Distribuição do Tempo de Execução para Soluções Encontradas', fontsize=16)
plt.xlabel('Algoritmo', fontsize=12)
plt.ylabel('Tempo de Execução (ms)', fontsize=12)
plt.xticks(fontsize=11)
plt.tight_layout()
plt.savefig('../boxplot_tempo.png')
print("\nGráfico 'boxplot_tempo.png' gerado com sucesso.")

# 2. Boxplot de Passos
plt.figure(figsize=(10, 6))
sns.boxplot(x='algoritmo', y='passos', data=df_sucesso, palette="pastel")
plt.title('Distribuição de Passos para Soluções Encontradas', fontsize=16)
plt.xlabel('Algoritmo', fontsize=12)
plt.ylabel('Número de Passos (Reinícios ou Movimentos Laterais)', fontsize=12)
plt.xticks(fontsize=11)
plt.tight_layout()
plt.savefig('../boxplot_passos.png')
print("Gráfico 'boxplot_passos.png' gerado com sucesso.")

# 3. Gráfico de Barras da Taxa de Sucesso
success_rate_df = df.groupby('algoritmo')['sucesso'].value_counts(normalize=True).unstack().fillna(0)
success_rate_df['taxa_sucesso'] = success_rate_df[1] * 100

plt.figure(figsize=(8, 6))
ax = sns.barplot(x=success_rate_df.index, y='taxa_sucesso', data=success_rate_df, palette="viridis")
plt.title('Taxa de Sucesso por Algoritmo', fontsize=16)
plt.xlabel('Algoritmo', fontsize=12)
plt.ylabel('Taxa de Sucesso (%)', fontsize=12)
plt.ylim(0, 105)
# Adicionar rótulos nas barras
for p in ax.patches:
    ax.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                textcoords='offset points')
plt.tight_layout()
plt.savefig('../taxa_sucesso.png')
print("Gráfico 'taxa_sucesso.png' gerado com sucesso.")