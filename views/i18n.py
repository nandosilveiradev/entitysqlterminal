# views/i18n.py

class I18n:
    def __init__(self, lang="en"):
        self.lang = lang

    def text(self, key):
        messages = {
            "mode_intro": {
                "pt": "Selecione o modo de operação. Essa escolha define como o programa vai funcionar.",
                "en": "Select the operation mode. This choice defines how the program will work."
            },
            "mode_options": {
                "pt": "1) Conectar ao servidor\n2) Gerar arquivos locais",
                "en": "1) Connect to server\n2) Generate local files"
            },
            "mode_selected": {
                "pt": "Modo selecionado:",
                "en": "Selected mode:"
            }
        }
        return messages.get(key, {}).get(self.lang, "")
