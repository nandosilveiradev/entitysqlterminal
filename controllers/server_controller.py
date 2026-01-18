# controller/server_controller.py

import psycopg2

class ServerController:
    def __init__(self, view, i18n):
        self.view = view
        self.i18n = i18n

    def ask_connection_data(self):
        self.view.show_message(self.i18n.server_questions())
        host = self.view.ask_input("Host: ")
        port = self.view.ask_input("Port: ")
        user = self.view.ask_input("User: ")
        password = self.view.ask_input("Password: ")
        database = self.view.ask_input("Database: ")
        return {"host": host, "port": port, "user": user, "password": password, "database": database}

    def test_connection(self, conn_data):
        try:
            conn = psycopg2.connect(**conn_data)
            self.view.show_message(self.i18n.connection_success())
            conn.close()
        except Exception as e:
            self.view.show_message(self.i18n.connection_failed())
            print(e)
