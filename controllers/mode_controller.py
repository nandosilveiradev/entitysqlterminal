class ModeController:
    def __init__(self, view, i18n):
        self.view = view
        self.i18n = i18n

    def choose_mode(self):
        self.view.show_message(self.i18n.mode_intro())
        self.view.show_message(self.i18n.mode_options())

        while True:
            choice = self.view.ask_input("> ").strip()
            if choice == "1":
                return "server"
            elif choice == "2":
                return "local"
            else:
                self.view.show_message(self.i18n.invalid_option())
