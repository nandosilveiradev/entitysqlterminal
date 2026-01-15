from views.cli_view import CLIView
from views.i18n import I18n
from controllers.mode_controller import ModeController
from controllers.server_controller import ServerController

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
    lang = choose_language()
    view = CLIView()
    i18n = I18n(lang)

    # Now ask for operation mode
    mode_controller = ModeController(view, i18n)
    mode = mode_controller.choose_mode()

    print(f"Selected mode: {mode}")
    
    if mode == "server":
        server_controller = ServerController(view, i18n)
        view.show_message(i18n.text("server_questions"))
        conn_data = server_controller.ask_connection_data()
        print("Connection data collected:", conn_data)
    else:
        view.show_message(i18n.text("local_selected"))
