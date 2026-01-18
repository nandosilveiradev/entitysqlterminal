# models/database.py

import sqlite3
import os

def generate_database(entities, filename="entitysql.db"):
    if os.path.exists(filename):
        os.remove(filename)

    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    for e in entities:
        cursor.execute(e.generate_sql())
        rel_sql = e.generate_relations_sql()
        if rel_sql:
            for stmt in rel_sql.split(";"):
                stmt = stmt.strip()
                if stmt:
                    cursor.execute(stmt)

    conn.commit()
    conn.close()
    print(f"Banco de dados gerado em {filename}")
