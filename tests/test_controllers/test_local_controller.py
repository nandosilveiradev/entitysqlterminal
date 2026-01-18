# tests/test_controllers/test_local_controller.py
import pytest
from controllers.local_controller import LocalController
from models.entity import Entity

class DummyView:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0
        self.messages = []

    def ask_input(self, prompt):
        # devolve valores pré-definidos
        if self.index < len(self.inputs):
            val = self.inputs[self.index]
            self.index += 1
            return val
        return ""
    
    def show_message(self, msg):
        self.messages.append(msg)

class DummyI18n:
    def ask_entity_name(self): return "Nome da entidade:"
    def empty_entity_name(self): return "Nome vazio!"
    def ask_attribute_name(self): return "Nome do atributo:"
    def attribute_list_done(self): return "Fim dos atributos."
    def entity_created(self): return "Entidade criada!"
    def ask_more_entities(self): return "Criar mais entidades?"

def test_local_controller_creates_entity():
    inputs = [
        "produto", "id", "1", "s", "s", "n", "s", "", "n"
    ]
    view = DummyView(inputs)
    i18n = DummyI18n()
    entities = []

    lc = LocalController(view=view, i18n=i18n, entities=entities)
    lc.create_entities("db_teste")

    assert len(entities) == 1
    e = entities[0]
    assert isinstance(e, Entity)
    assert e.name == "produto"

    # Verifica se existe um atributo chamado "id"
    assert any(attr["name"] == "id" for attr in e.attributes)

    # Pega o atributo "id" e valida os detalhes
    id_attr = next(attr for attr in e.attributes if attr["name"] == "id")
    assert id_attr["type"] == "INTEGER"
    assert id_attr["primary_key"] is True
    assert id_attr["auto_increment"] is True
    assert id_attr["unique"] is True
    assert id_attr["not_null"] is True
