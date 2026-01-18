# entity-sql-cli.py

from controllers.tmux_controller import ensure_tmux_installed, start_or_attach_session
from app import App

if __name__ == "__main__":
    ensure_tmux_installed()
    start_or_attach_session()

    app = App()
    app.run()
