# controller/local_controller.py

from models.entity import Entity

class LocalController:
    def __init__(self, view, i18n, entities, lang="pt"):
        self.view = view
        self.i18n = i18n
        self.entities = entities
        self.lang = lang

    def ask_choice(self, prompt, options):
        while True:
            choice = self.view.ask_input(prompt).strip()
            if choice in options:
                return options[choice]
            else:
                self.view.show_message("⚠️ Opção inválida, tente novamente." if self.lang == "pt" else "⚠️ Invalid option, please try again.")

    def ask_yes_no(self, prompt):
        while True:
            answer = self.view.ask_input(prompt).strip().lower()
            if answer in ["s", "y"]:
                return True
            elif answer in ["n"]:
                return False
            else:
                self.view.show_message("⚠️ Resposta inválida, digite 's' ou 'n'." if self.lang == "pt" else "⚠️ Invalid answer, type 'y' or 'n'.")

    def create_entities(self, db_name):
        while True:
            name = self.view.ask_input(self.i18n.ask_entity_name()).strip()
            if not name:
                self.view.show_message(self.i18n.empty_entity_name())
                break

            entity = Entity(name)

            while True:
                attr_name = self.view.ask_input(self.i18n.ask_attribute_name()).strip()
                if not attr_name:
                    self.view.show_message(self.i18n.attribute_list_done())
                    break

                print("Escolha o tipo do atributo:")
                print("1) INTEGER")
                print("2) VARCHAR")
                print("3) TEXT")
                print("4) DATE")
                print("5) DECIMAL")

                types = {"1": "INTEGER", "2": "VARCHAR", "3": "TEXT", "4": "DATE", "5": "DECIMAL"}
                attr_type = self.ask_choice("Digite o número da opção: ", types)

                length, precision, scale = None, None, None
                primary_key, auto_increment = False, False

                if attr_type == "VARCHAR":
                    length = self.view.ask_input("Digite o tamanho (1 a 255): ").strip()
                    length = int(length) if length.isdigit() else None

                elif attr_type == "DECIMAL":
                    precision = self.view.ask_input("Digite a precisão (ex: 10): ").strip()
                    precision = int(precision) if precision.isdigit() else None
                    scale = self.view.ask_input("Digite a escala (ex: 2): ").strip()
                    scale = int(scale) if scale.isdigit() else None

                elif attr_type == "INTEGER":
                    primary_key = self.ask_yes_no("Esse atributo deve ser PRIMARY KEY? (s/n): ")
                    if primary_key:
                        auto_increment = self.ask_yes_no("Esse atributo deve ser AUTO INCREMENT? (s/n): ")

                not_null = not self.ask_yes_no("Esse atributo pode ser NULL? (s/n): ")
                unique = self.ask_yes_no("Esse atributo deve ser UNIQUE? (s/n): ")

                entity.add_attribute(
                    attr_name,
                    attr_type,
                    length=length,
                    precision=precision,
                    scale=scale,
                    not_null=not_null,
                    unique=unique,
                    primary_key=primary_key,
                    auto_increment=auto_increment
                )

            self.entities.append(entity)
            self.view.show_message(self.i18n.entity_created())

            again = self.ask_yes_no(self.i18n.ask_more_entities())
            if not again:
                break
