# controller/normalization_controller.py

class NormalizationController:
    def __init__(self, view, i18n, entities):
        self.view = view
        self.i18n = i18n
        self.entities = entities
        self.relations = {}

    def normalize_relations(self):
        for i, entity_a in enumerate(self.entities):
            for j, entity_b in enumerate(self.entities):
                if i == j:
                    continue  # não relaciona consigo mesmo

                # 🔹 Pergunta inicial: dependência existencial
                exist = self.view.ask_input(
                    self.i18n.ask_relation_exist(entity_a.name, entity_b.name)
                ).strip().lower()

                if exist in ["s", "y"]:
                    # Se pode existir sem → relação opcional
                    rel_type = "opcional"
                    key = f"{entity_a.name}_{entity_b.name}"
                    self.relations[key] = rel_type
                    self.view.show_message(
                        self.i18n.relation_result(entity_a.name, entity_b.name, rel_type)
                    )
                    continue  # não precisa perguntar mais nada

                # 🔹 Se não pode existir sem → relação obrigatória
                many = self.view.ask_input(
                    self.i18n.ask_relation_many(entity_a.name, entity_b.name)
                ).strip().lower()

                if many in ["s", "y"]:
                    rel_type = "1:N"
                else:
                    rel_type = "1:1"

                key = f"{entity_a.name}_{entity_b.name}"
                self.relations[key] = rel_type

                self.view.show_message(
                    self.i18n.relation_result(entity_a.name, entity_b.name, rel_type)
                )

                # 🔹 Se for N:N (detectado pelo inverso), perguntar sobre tabela extra
                if rel_type == "N:N":
                    rel_table = f"{entity_a.name}_{entity_b.name}"
                    extra = self.view.ask_input(
                        self.i18n.ask_relation_extra_table(entity_a.name, entity_b.name, rel_table)
                    ).strip().lower()
                    if extra in ["s", "y"]:
                        self.view.show_message(f"Tabela {rel_table} criada para relação N:N.")
