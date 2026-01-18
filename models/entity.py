# model/entity.py

class Entity:
    def __init__(self, name):
        self.name = name
        self.attributes = []

    def add_attribute(self, name, attr_type, length=None, precision=None, scale=None,
                      not_null=False, unique=False, primary_key=False, auto_increment=False):
        self.attributes.append({
            "name": name,
            "type": attr_type,
            "length": length,
            "precision": precision,
            "scale": scale,
            "not_null": not_null,
            "unique": unique,
            "primary_key": primary_key,
            "auto_increment": auto_increment
        })

    def generate_sql(self):
        cols = []
        for attr in self.attributes:
            col_def = f"{attr['name']} {attr['type']}"

            # 🔹 Tipos com tamanho
            if attr["type"] == "VARCHAR" and attr["length"]:
                col_def = f"{attr['name']} VARCHAR({attr['length']})"
            elif attr["type"] == "DECIMAL" and attr["precision"] and attr["scale"] is not None:
                col_def = f"{attr['name']} DECIMAL({attr['precision']},{attr['scale']})"

            # 🔹 Restrições
            if attr["not_null"]:
                col_def += " NOT NULL"
            if attr["unique"]:
                col_def += " UNIQUE"

            # 🔹 PRIMARY KEY
            if attr["primary_key"]:
                col_def += " PRIMARY KEY"

                # 🔹 AUTOINCREMENT só se for INTEGER PRIMARY KEY
                if attr["auto_increment"] and attr["type"] == "INTEGER":
                    col_def += " AUTOINCREMENT"

            cols.append(col_def)

        sql = f"CREATE TABLE {self.name} ({', '.join(cols)});"
        return sql

    def generate_relations_sql(self):
        # Placeholder para futuras relações
        return ""
