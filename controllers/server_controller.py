# controllers/server_controller.py

class ServerController:
    def __init__(self, view, i18n):
        self.view = view
        self.i18n = i18n

    def ask_connection_data(self):
        host = self.view.ask_input("Host (default: localhost): ") or "localhost"
        port = self.view.ask_input("Port (default: 5000): ") or "5000"
        user = self.view.ask_input("User (default: nando): ") or "nando"
        password = self.view.ask_input("Password (default: secret): ") or "secret"
        database = self.view.ask_input("Database (default: entitydb): ") or "entitydb"

        return {
            "host": host,
            "port": port,
            "user": user,
            "password": password,
            "database": database
        }
