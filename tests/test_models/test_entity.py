# tests/test_models/test_entity.py
import pytest
from models.entity import Entity

def test_entity_sql_generation():
    e = Entity("cliente")
    e.add_attribute("id", "INTEGER", primary_key=True, auto_increment=True, unique=True)
    e.add_attribute("name", "VARCHAR(111)", not_null=True)

    sql = e.generate_sql()
    assert "CREATE TABLE cliente" in sql
    assert "id INTEGER" in sql
    assert "PRIMARY KEY" in sql
    assert "AUTOINCREMENT" in sql
    assert "UNIQUE" in sql
    assert "name VARCHAR(111) NOT NULL" in sql
