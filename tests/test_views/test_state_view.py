# tests/test_views/test_state_view.py
import os
from views import state_view
from models.entity import Entity

def test_state_view_updates_file(tmp_path):
    # Trocar diretório atual para tmp_path
    cwd = os.getcwd()
    os.chdir(tmp_path)

    try:
        # Criar entidade de teste
        e1 = Entity("cliente")
        e1.add_attribute("id", "INTEGER", primary_key=True, auto_increment=True, unique=True)
        e1.add_attribute("nome", "VARCHAR(255)", not_null=True)

        entities = [e1]
        relations = {"cliente_pedido": "1:N"}

        # Executar função
        state_view.update_view_state("db_teste", entities, relations)

        # Verificar arquivo
        file_path = tmp_path / "view_state.txt"
        assert file_path.exists()

        content = file_path.read_text()
        assert "Banco: db_teste" in content
        assert "Entidade: cliente" in content
        assert "- id INTEGER PRIMARY_KEY AUTOINCREMENT UNIQUE" in content
        assert "- nome VARCHAR(255) NOT NULL" in content
        assert "Relações:" in content
        assert "- cliente ↔ pedido 1:N" in content
    finally:
        os.chdir(cwd)
