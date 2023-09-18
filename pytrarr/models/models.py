import sqlite3

from dataclasses import asdict
from pytrarr.utils.dataclass import MediaContent


# Insere os dados no banco de dados SQLite
def add_content_in_database(media_content: MediaContent):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Converta o objeto (por exemplo, Movie) para um dicionário antes de inserir no banco de dados
    item_dict = asdict(media_content)
    
    # Insira os dados no banco de dados SQLite
    # Substitua esta parte com sua lógica de inserção real
    cursor.execute("INSERT INTO media_content (...) VALUES (...)")  # Exemplo para filmes
            
    conn.commit()
    conn.close()


