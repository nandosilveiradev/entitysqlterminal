import sys
import readline

from views.cli_view import CLIView
from views.i18n import I18n
from controllers.mode_controller import ModeController
from controllers.server_controller import ServerController
from controllers.connection_tester import ConnectionTester
from controllers.local_controller import LocalController
from models.entity_manager import EntityManager
from controllers.tmux_controller import ensure_tmux_installed, start_or_attach_session


def choose_language():
    print("Select the language. This choice is only for program instructions.")
    print("It does not change the database or the generated files.\n")
    print("1) Português")
    print("2) English")
    choice = input("> ").strip()
    if choice == "2":
        return "en"
    return "pt"

if __name__ == "__main__":

    ensure_tmux_installed() 
       
    if "--inside-tmux" in sys.argv:
        # já estamos dentro da sessão, não chamar start_or_attach_session
        pass
    else:
        from controllers.tmux_controller import start_or_attach_session
        start_or_attach_session()
        sys.exit(0)  # encerra aqui, porque o attach já cuida de rodar


    # Escolha de idioma
    lang = choose_language()
    view = CLIView()
    i18n = I18n(lang)

    # Escolha de modo
    mode_controller = ModeController(view, i18n)
    mode = mode_controller.choose_mode()
    print(f"Selected mode: {mode}")

    # Gerenciador de entidades
    entity_manager = EntityManager()

    if mode == "server":
        # Pergunta dados de conexão
        server_controller = ServerController(view, i18n)
        view.show_message(i18n.text("server_questions"))
        conn_data = server_controller.ask_connection_data()
        print("Connection data collected:", conn_data)

        # Testa conexão
        tester = ConnectionTester(view, i18n)
        tester.test_connection(conn_data)

        # Exemplo: usar entidades já criadas
        print("Entidades atuais:", entity_manager.list_entities())
        for sql in entity_manager.generate_sql():
            print(sql)

    else:
        # Fluxo local: criar entidades/atributos
        view.show_message(i18n.text("local_selected"))
        local_controller = LocalController(view, i18n, entity_manager)
        local_controller.create_entities()

        # Mostrar entidades e SQL gerado
        print("Entidades criadas:", entity_manager.list_entities())
        for sql in entity_manager.generate_sql():
            print(sql)
