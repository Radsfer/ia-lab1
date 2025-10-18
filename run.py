import sys
import subprocess
import os
import venv

VENV_NAME = ".venv"


def run_command(command, shell=False):
    """Executa um comando no terminal e lida com erros."""
    try:
        print(f"--- Executando: {' '.join(command)} ---")
        subprocess.run(command, check=True, shell=shell)
    except subprocess.CalledProcessError as e:
        print(f"ERRO ao executar o comando: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"ERRO: Comando '{command[0]}' não encontrado. Verifique se está no seu PATH.")
        sys.exit(1)


def main():
    """Script para automatizar a instalação de dependências e execução do projeto."""
    if sys.version_info < (3, 6):
        print("ERRO: Este projeto requer Python 3.6 ou superior.")
        sys.exit(1)

    # --- INÍCIO DA CORREÇÃO ---
    # Encontra o diretório raiz do projeto (onde o script run.py está)
    project_root = os.path.dirname(os.path.abspath(__file__))

    # Constrói caminhos absolutos baseados na raiz do projeto
    venv_path = os.path.join(project_root, VENV_NAME)
    requirements_path = os.path.join(project_root, "requirements.txt")
    main_script_path = os.path.join(project_root, "trabalho1", "src", "main.py")
    # --- FIM DA CORREÇÃO ---

    # 1. Criação do Ambiente Virtual (usando o caminho absoluto)
    if not os.path.exists(venv_path):
        print(f"### Criando ambiente virtual em '{venv_path}'...")
        venv.create(venv_path, with_pip=True)
    else:
        print(f"### Ambiente virtual em '{venv_path}' já existe.")

    # Define os caminhos dos executáveis do venv de forma multiplataforma
    if sys.platform == "win32":
        pip_executable = os.path.join(venv_path, "Scripts", "pip")
        python_executable = os.path.join(venv_path, "Scripts", "python")
    else:  # Linux, macOS, etc.
        pip_executable = os.path.join(venv_path, "bin", "pip")
        python_executable = os.path.join(venv_path, "bin", "python")

    # 2. Instalação das dependências (usando o caminho absoluto)
    print("### Instalando dependências do requirements.txt...")
    run_command([pip_executable, "install", "-r", requirements_path])

    # 3. Execução do script principal (usando o caminho absoluto)
    print("### Executando o script principal para gerar os resultados...")
    run_command([python_executable, main_script_path])

    print("\n### Processo finalizado com sucesso!")
    print(f"### Os resultados foram gerados na pasta 'trabalho1/'.")
    print(f"### Para ativar o ambiente virtual manualmente, use:")
    if sys.platform == "win32":
        print(f"    {os.path.relpath(venv_path)}\\Scripts\\activate")
    else:
        print(f"    source {os.path.relpath(venv_path)}/bin/activate")


if __name__ == "__main__":
    main()