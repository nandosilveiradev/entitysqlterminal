# views/state_view.py

def update_view_state(db_name, entities, relations):
    with open("view_state.txt", "w", encoding="utf-8") as f:
        f.write(f"Banco: {db_name}\n\n")
        for e in entities:
            f.write(f"Entidade: {e.name}\n")
            for attr in e.attributes:
                line = f"  - {attr['name']} {attr['type']}"
                if attr.get("primary_key"):
                    line += " PRIMARY_KEY"
                if attr.get("auto_increment"):
                    line += " AUTOINCREMENT"
                if attr.get("unique"):
                    line += " UNIQUE"
                if attr.get("not_null"):
                    line += " NOT NULL"
                f.write(line + "\n")
            f.write("\n")
        if relations:
            f.write("Relações:\n")
            for k, v in relations.items():
                f.write(f"- {k.replace('_',' ↔ ')} {v}\n")
