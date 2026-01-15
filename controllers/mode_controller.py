# controllers/mode_controller.py

class ModeController:
    def __init__(self, view, i18n):
        self.view = view
        self.i18n = i18n

    def choose_mode(self):
        self.view.show_message(self.i18n.text("mode_intro"))
        self.view.show_message(self.i18n.text("mode_options"))

        choice = self.view.ask_input("> ").strip()
        if choice == "1":
            return "server"
        return "local"
