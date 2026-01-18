# tests/test_controllers/test_normalization_controller.py
from controllers.normalization_controller import NormalizationController
from models.entity import Entity

class DummyView:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0
        self.messages = []

    def ask_input(self, prompt):
        # devolve valores pré-definidos
        val = self.inputs[self.index]
        self.index += 1
        return val

    def show_message(self, msg):
        self.messages.append(msg)

class DummyI18n:
    def ask_relation_exist(self, a, b): return f"{a} depende de {b}?"
    def ask_relation_many(self, a, b): return f"{a} tem muitos {b}?"
    def relation_result(self, a, b, rel): return f"Relação {a}-{b}: {rel}"
    def ask_relation_extra_table(self, a, b, rel_table): return f"Tabela extra {rel_table}?"

def test_normalization_controller_relations():
    # Criar duas entidades
    e1 = Entity("cliente")
    e1.add_attribute("id", "INTEGER", primary_key=True)

    e2 = Entity("pedido")
    e2.add_attribute("id", "INTEGER", primary_key=True)

    # Simular respostas:
    # Primeiro par (cliente, pedido): "n" → não pode existir sem → pergunta many → "s" → 1:N
    # Segundo par (pedido, cliente): "s" → pode existir sem → opcional
    inputs = ["n", "s", "s"]  # ordem das chamadas ask_input
    view = DummyView(inputs)
    i18n = DummyI18n()

    nc = NormalizationController(view=view, i18n=i18n, entities=[e1, e2])
    nc.normalize_relations()

    # Verifica se as relações foram criadas
    assert "cliente_pedido" in nc.relations
    assert nc.relations["cliente_pedido"] == "1:N"

    assert "pedido_cliente" in nc.relations
    assert nc.relations["pedido_cliente"] == "opcional"

    # Verifica se mensagens foram registradas
    assert any("Relação cliente-pedido: 1:N" in m for m in view.messages)
    assert any("Relação pedido-cliente: opcional" in m for m in view.messages)
