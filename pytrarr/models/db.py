import sqlite3


def create_media_database_table():
    conn = sqlite3.connect("media_database.db")
    cursor = conn.cursor()

    # Definir os comandos SQL para criar as tabelas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS media_content (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        genres TEXT,
        poster TEXT,
        uploaded TEXT,
        release_date TEXT,
        duration TEXT,
        size TEXT,
        imdb TEXT,
        last_update TEXT
    )
    '''
    )

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS season (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        season_number TEXT,
        media_content_id INTEGER,
        FOREIGN KEY(media_content_id) REFERENCES media_content(id)
    )
    '''
    )

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS episode (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        season_number TEXT,
        episode_number TEXT,
        duration TEXT,
        size TEXT,
        season_id INTEGER,
        FOREIGN KEY(season_id) REFERENCES season(id)
    )
    '''
    )

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS torrent (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        languages TEXT,
        subtitles TEXT,
        size TEXT,
        video_format TEXT,
        quality TEXT,
        quality_video TEXT,
        quality_audio TEXT,
        info_hash TEXT,
        file_content TEXT,
        media_content_id INTEGER,
        episode_id INTEGER,
        FOREIGN KEY(media_content_id) REFERENCES media_content(id),
        FOREIGN KEY(episode_id) REFERENCES episode(id)
    )
    '''
    )

    conn.commit()
    conn.close()
    
    
# Execute as funções de criação das tabelas
if __name__ == "__main__":
    create_media_database_table()