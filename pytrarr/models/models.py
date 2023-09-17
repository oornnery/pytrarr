import sqlite3

# Criação da tabela para filmes
def create_movies_table():
    conn = sqlite3.connect("media_database.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            poster TEXT,
            release_date TEXT,
            uploaded TEXT,
            genres TEXT,
            languages TEXT,
            duration TEXT,
            quality TEXT,
            audio TEXT,
            video TEXT,
            format TEXT,
            size TEXT,
            subtitles TEXT,
            imdb TEXT,
            last_update TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Criação da tabela para séries
def create_series_table():
    conn = sqlite3.connect("media_database.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS series (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            poster TEXT,
            release_date TEXT,
            uploaded TEXT,
            genres TEXT,
            languages TEXT,
            duration TEXT,
            quality TEXT,
            audio TEXT,
            video TEXT,
            format TEXT,
            size TEXT,
            subtitles TEXT,
            imdb TEXT,
            last_update TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Execute as funções de criação das tabelas
if __name__ == "__main__":
    create_movies_table()
    create_series_table()
    # Adicione chamadas para criar tabelas para outras categorias (novela, anime, música, ebook) da mesma maneira
