# tests/test_integration/test_full_flow.py
import os
from controllers.local_controller import LocalController
from controllers.normalization_controller import NormalizationController
from views import state_view
from models.entity import Entity

class DummyView:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0
        self.messages = []

    def ask_input(self, prompt):
        val = self.inputs[self.index]
        self.index += 1
        return val

    def show_message(self, msg):
        self.messages.append(msg)

class DummyI18n:
    def ask_entity_name(self): return "Nome da entidade:"
    def empty_entity_name(self): return "Nome vazio!"
    def ask_attribute_name(self): return "Nome do atributo:"
    def attribute_list_done(self): return "Fim dos atributos."
    def entity_created(self): return "Entidade criada!"
    def ask_more_entities(self): return "Criar mais entidades?"
    def ask_relation_exist(self, a, b): return f"{a} depende de {b}?"
    def ask_relation_many(self, a, b): return f"{a} tem muitos {b}?"
    def relation_result(self, a, b, rel): return f"Relação {a}-{b}: {rel}"
    def ask_relation_extra_table(self, a, b, rel_table): return f"Tabela extra {rel_table}?"

def test_full_flow(tmp_path):
    # Simular entradas: entidade "cliente" com atributo "id INTEGER PK AI UNIQUE NOT NULL"
    inputs = [
        "cliente", "id", "1", "s", "s", "n", "s", "", "n",  # entidade e atributos
        "n", "s", "s"  # respostas para normalize_relations
    ]
    view = DummyView(inputs)
    i18n = DummyI18n()
    entities = []

    # 1. Criar entidade
    lc = LocalController(view=view, i18n=i18n, entities=entities)
    lc.create_entities("db_teste")
    assert len(entities) == 1
    e = entities[0]
    assert e.name == "cliente"

    # 2. Normalizar relações (com outra entidade fictícia)
    e2 = Entity("pedido")
    e2.add_attribute("id", "INTEGER", primary_key=True)
    entities.append(e2)

    nc = NormalizationController(view=view, i18n=i18n, entities=entities)
    nc.normalize_relations()
    assert "cliente_pedido" in nc.relations

    # 3. Salvar estado
    cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        state_view.update_view_state("db_teste", entities, nc.relations)
        file_path = tmp_path / "view_state.txt"
        assert file_path.exists()
        content = file_path.read_text()
        assert "Banco: db_teste" in content
        assert "Entidade: cliente" in content
        assert "Entidade: pedido" in content
        assert "Relações:" in content
    finally:
        os.chdir(cwd)
# tests/test_integration/test_full_flow.py
import os
from controllers.local_controller import LocalController
from controllers.normalization_controller import NormalizationController
from views import state_view
from models.entity import Entity

class DummyView:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0
        self.messages = []

    def ask_input(self, prompt):
        val = self.inputs[self.index]
        self.index += 1
        return val

    def show_message(self, msg):
        self.messages.append(msg)

class DummyI18n:
    def ask_entity_name(self): return "Nome da entidade:"
    def empty_entity_name(self): return "Nome vazio!"
    def ask_attribute_name(self): return "Nome do atributo:"
    def attribute_list_done(self): return "Fim dos atributos."
    def entity_created(self): return "Entidade criada!"
    def ask_more_entities(self): return "Criar mais entidades?"
    def ask_relation_exist(self, a, b): return f"{a} depende de {b}?"
    def ask_relation_many(self, a, b): return f"{a} tem muitos {b}?"
    def relation_result(self, a, b, rel): return f"Relação {a}-{b}: {rel}"
    def ask_relation_extra_table(self, a, b, rel_table): return f"Tabela extra {rel_table}?"

def test_full_flow(tmp_path):
    # Simular entradas: entidade "cliente" com atributo "id INTEGER PK AI UNIQUE NOT NULL"
    inputs = [
        "cliente", "id", "1", "s", "s", "n", "s", "", "n",  # entidade e atributos
        "n", "s", "s"  # respostas para normalize_relations
    ]
    view = DummyView(inputs)
    i18n = DummyI18n()
    entities = []

    # 1. Criar entidade
    lc = LocalController(view=view, i18n=i18n, entities=entities)
    lc.create_entities("db_teste")
    assert len(entities) == 1
    e = entities[0]
    assert e.name == "cliente"

    # 2. Normalizar relações (com outra entidade fictícia)
    e2 = Entity("pedido")
    e2.add_attribute("id", "INTEGER", primary_key=True)
    entities.append(e2)

    nc = NormalizationController(view=view, i18n=i18n, entities=entities)
    nc.normalize_relations()
    assert "cliente_pedido" in nc.relations

    # 3. Salvar estado
    cwd = os.getcwd()
    os.chdir(tmp_path)
    try:
        state_view.update_view_state("db_teste", entities, nc.relations)
        file_path = tmp_path / "view_state.txt"
        assert file_path.exists()
        content = file_path.read_text()
        assert "Banco: db_teste" in content
        assert "Entidade: cliente" in content
        assert "Entidade: pedido" in content
        assert "Relações:" in content
    finally:
        os.chdir(cwd)
