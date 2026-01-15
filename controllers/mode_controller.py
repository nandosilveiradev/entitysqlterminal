class ModeController:
    def __init__(self, view, i18n):
        self.view = view
        self.i18n = i18n

    def escolher_modo(self):
        self.view.show_message(self.i18n.ask_mode())
        opcoes = [
            self.i18n.option_server(),
            self.i18n.option_local()
        ]

        for i, opt in enumerate(opcoes, start=1):
            self.view.show_message(f"{i}) {opt}")

        while True:
            escolha = self.view.ask_input("> ")
            if escolha == "1":
                return "server"
            elif escolha == "2":
                return "local"
            else:
                self.view.show_message(self.i18n.invalid_option())
