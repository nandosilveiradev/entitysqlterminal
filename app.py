# app.py 

import os
from views.cli_view import CLIView
from views.i18n import I18n
from views.state_view import update_view_state   
from controllers.server_controller import ServerController
from controllers.local_controller import LocalController
from controllers.normalization_controller import NormalizationController
from models.database import generate_database

class App:
    def __init__(self):
        self.view = CLIView()
        self.lang = self.choose_language()
        self.i18n = I18n(self.lang)
        self.entities = []

    def choose_language(self):
        self.view.show_message(self.i18n.language_intro())
        self.view.show_message(self.i18n.language_options())
        choice = self.view.ask_input("> ").strip()
        return "en" if choice == "2" else "pt"

    def list_databases(self):
        dbs = [f for f in os.listdir(".") if f.endswith(".db")]
        if dbs:
            self.view.show_message(self.i18n.list_databases(dbs))
        else:
            self.view.show_message("Nenhum banco criado ainda." if self.lang == "pt" else "No databases created yet.")

    def run(self):
        while True:
            self.view.show_message(self.i18n.main_menu())
            choice = self.view.ask_input("> ").strip()

            if choice == "1":
                server_controller = ServerController(self.view, self.i18n)
                conn_data = server_controller.ask_connection_data()
                server_controller.test_connection(conn_data)

            elif choice == "2":
                db_name = self.view.ask_input("Digite o nome do banco de dados (ex: meu_banco.db): ").strip()
                if not db_name:
                    db_name = "entitysql.db"
                if not db_name.endswith(".db"):
                    db_name += ".db"

                local_controller = LocalController(self.view, self.i18n, self.entities)
                local_controller.create_entities(db_name)

                update_view_state(db_name, self.entities, {})

                normalizer = NormalizationController(self.view, self.i18n, self.entities)
                normalizer.normalize_relations()

                update_view_state(db_name, self.entities, normalizer.relations)

                generate_database(self.entities, filename=db_name)

                self.view.show_message(self.i18n.sql_generated())
                for e in self.entities:
                    print(e.generate_sql())
                    print(e.generate_relations_sql())

                update_view_state(db_name, self.entities, normalizer.relations)

                self.list_databases()

            elif choice == "3":
                self.view.show_message(self.i18n.goodbye())
                break

            else:
                self.view.show_message(self.i18n.invalid_option())
