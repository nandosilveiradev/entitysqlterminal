class I18n:
    def __init__(self, lang="pt"):
        self.lang = lang

    def ask_mode(self):
        return {
            "pt": "Você deseja conectar este programa a um servidor de banco de dados (MySQL, PostgreSQL, etc.) para criar as tabelas diretamente nele, ou prefere trabalhar apenas localmente gerando os arquivos (schema.sql, dictionary.json) para enviar manualmente depois?",
            "en": "Do you want to connect this program to a database server (MySQL, PostgreSQL, etc.) to create tables directly, or do you prefer working locally generating files (schema.sql, dictionary.json) to send manually later?"
        }[self.lang]

    def option_server(self):
        return {"pt": "Conectar a um servidor de banco de dados", "en": "Connect to a database server"}[self.lang]

    def option_local(self):
        return {"pt": "Gerar arquivos localmente", "en": "Generate files locally"}[self.lang]

    def invalid_option(self):
        return {"pt": "Opção inválida, escolha 1 ou 2.", "en": "Invalid option, choose 1 or 2."}[self.lang]
