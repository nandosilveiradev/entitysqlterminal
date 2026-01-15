# views/cli_view.py

class CLIView:
    def show_message(self, message):
        print(message)

    def ask_input(self, prompt):
        return input(prompt)
