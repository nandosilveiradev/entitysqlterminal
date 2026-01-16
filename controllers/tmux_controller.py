import os
import subprocess
import sys

SESSION_NAME = "EntitySqlTerminal"

def ensure_tmux_installed():
    try:
        subprocess.run(["tmux", "-V"], check=True, capture_output=True)
    except Exception:
        print("tmux não encontrado. Instale manualmente com:")
        print("sudo apt-get update && sudo apt-get install -y tmux")
        sys.exit(1)

def start_or_attach_session():
    project_root = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(project_root, "..", "tmux", "tmuxEntitySQLTerminal.conf")

    # Verifica se a sessão já existe
    result = subprocess.run(["tmux", "has-session", "-t", SESSION_NAME],
                            capture_output=True)
    if result.returncode != 0:
        script_path = os.path.abspath(sys.argv[0])
        # Cria a sessão e já carrega o config ANTES de rodar o Python
        subprocess.run([
            "tmux", "new-session", "-d", "-s", SESSION_NAME,
            f"bash -c 'tmux source-file {config_path}; exec python3 {script_path} --inside-tmux'"
        ], check=True)

    subprocess.run(["tmux", "attach", "-t", SESSION_NAME], check=True)
