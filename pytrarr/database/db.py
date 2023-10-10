import sqlite3
import uuid

from click import option

class MyDataBase:
    def __init__(self) -> None:
        # Cursor
        self.conn = sqlite3.connect("pytrarr/database/database.db")
        self.cursor = self.conn.cursor()

    def create_table_tv_show(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tv_show (
            id TEXT PRIMARY KEY,
            q TEXT,
            season INTEGER,
            ep INTEGER,
            year INTEGER,
            genre TEXT,
            imdbid TEXT,
            tmdbid TEXT,
            torrent TEXT,
            seeds INTEGER,
            checked INTEGER
        )
        ''')

    def create_table_movie(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS movie (
            id TEXT PRIMARY KEY,
            q TEXT,
            year INTEGER,
            genre TEXT,
            imdbid TEXT,
            tmdbid TEXT,
            torrent TEXT,
            seeds INTEGER,
            checked INTEGER
        )
        ''')

    def create_table_music(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS music (
            id TEXT PRIMARY KEY,
            q TEXT,
            album TEXT,
            artist TEXT,
            label TEXT,
            year INTEGER,
            genre TEXT,
            imdbid TEXT,
            tmdbid TEXT,
            torrent TEXT,
            seeds INTEGER,
            checked INTEGER
        )
        ''')

    def create_table_book(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS music (
            id TEXT PRIMARY KEY,
            q TEXT,
            title TEXT,
            author TEXT,
            publisher TEXT,
            year INTEGER,
            genre TEXT,
            imdbid TEXT,
            tmdbid TEXT,
            torrent TEXT,
            seeds INTEGER,
            checked INTEGER
        )
        ''')

    def commit(self):
        self.conn.commit()
    
    def close(self):
        self.conn.close()
    
    def generate_unique_uuid(self, table_name):
        while True:
            unique_id = str(uuid.uuid4())
            self.cursor.execute(f'SELECT id FROM {table_name} WHERE id = ?', (unique_id,))
            existing_id = self.cursor.fetchone()
            if not existing_id:
                return unique_id
    
    def add_tv_show(self, 
            q: str, 
            season: int, 
            ep: int, 
            year: int, 
            genre: str,
            imdbid: int, 
            tmdbid: int, 
            torrent: str, 
            checked: bool = False, 
            seeds: int = 0
        ):
        generate_id = self.generate_unique_uuid('tv_show')
        self.cursor.execute('''
            INSERT INTO tv_show (id, q, season, ep, year, genre, imdbid, tmdbid, torrent, seeds, checked)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (generate_id, q, season, ep, year, genre, imdbid, tmdbid, torrent, seeds, checked))
        self.commit()
    
    def add_movie(self, 
            q: str, 
            year: int, 
            genre: str,
            imdbid: int, 
            tmdbid: int, 
            torrent: str, 
            checked: bool = False, 
            seeds: int = 0
        ):
        generate_id = self.generate_unique_uuid('tv_show')
        self.cursor.execute('''
            INSERT INTO tv_show (id, q, year, genre, imdbid, tmdbid, torrent, seeds, checked)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (generate_id, q, year, genre, imdbid, tmdbid, torrent, seeds, checked))
        self.commit()

    def add_music(self, 
            q: str,
            album: str,
            artist: str,
            label: str, 
            year: int, 
            genre: str,
            imdbid: int, 
            tmdbid: int, 
            torrent: str, 
            checked: bool = False, 
            seeds: int = 0
        ):
        generate_id = self.generate_unique_uuid('tv_show')
        self.cursor.execute('''
            INSERT INTO tv_show (id, q, album, artist, label, year, genre, imdbid, tmdbid, torrent, seeds, checked)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (generate_id, q, album, artist, label, year, genre, imdbid, tmdbid, torrent, seeds, checked))
        self.commit()

    def add_book(self, 
            q: str,
            title: str,
            author: str,
            publisher: str, 
            year: int, 
            genre: str,
            imdbid: int, 
            tmdbid: int, 
            torrent: str, 
            checked: bool = False, 
            seeds: int = 0
        ):
        generate_id = self.generate_unique_uuid('tv_show')
        self.cursor.execute('''
            INSERT INTO tv_show (id, q, title, author, publisher, year, genre, imdbid, tmdbid, torrent, seeds, checked)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (generate_id, q, title, author, publisher, year, genre, imdbid, tmdbid, torrent, seeds, checked))
        self.commit()
    
    def search(self, q: str):
        self.cursor.execute('''
            SELECT * FROM tv_show WHERE q LIKE ?
            UNION ALL
            SELECT * FROM movie WHERE q LIKE ?
            UNION ALL
            SELECT * FROM music WHERE q LIKE ?
            UNION ALL
            SELECT * FROM book WHERE q LIKE ?
        ''', (f'%{q}%', f'%{q}%', f'%{q}%', f'%{q}%'))
        return self.cursor.fetchall()

    def search_tv_show(self, 
            q: str, 
            season: str = None, 
            ep: int = None,
            imdbid: str = None, 
            tmdbid: str = None, 
            year: int = None, 
            genre: str = None
        ):
        optional_fields = {
            'q': q,
            'season': season,
            'ep': ep,
            'imdbid': imdbid,
            'tmdbid': tmdbid,
            'year': year,
            'genre': genre
        }
        # Run sql building 
        sql_query, query_params = self.sql_building(optional_fields)
        # Return a consulting.
        return self.run_consulting(sql_query, query_params)
        
    def search_movie(self, 
            q: str, 
            year: str = None, 
            genre: str = None,
            imdbid: str = None, 
            tmdbid: str = None,
        ):
        
        optional_fields = {
            'q': q,
            'year': year,
            'genre': genre,
            'imdbid': imdbid,
            'tmdbid': tmdbid
        }
        # Run sql building 
        sql_query, query_params = self.sql_building(optional_fields)
        # Return a consulting.
        return self.run_consulting(sql_query, query_params)

    def search_music(self, 
        q: str, 
        album: str = None, 
        artist: str = None, 
        label: str = None, 
        year: str = None,
        genre: str = None,
        imdbid: str = None, 
        tmdbid: str = None,
        ):
        optional_fields = {
            'q': q,
            'album': album,
            'artist': artist,
            'label': label,
            'year': year,
            'genre': genre,
            'imdbid': imdbid,
            'tmdbid': tmdbid
        }
        # Run sql building 
        sql_query, query_params = self.sql_building(optional_fields)
        # Return a consulting.
        return self.run_consulting(sql_query, query_params)

    def search_book(self, 
        q: str = None, 
        title: str = None, 
        author: str = None, 
        publisher: str = None, 
        year: str = None,
        genre: str = None,
        imdbid: str = None, 
        tmdbid: str = None,
        ):
        optional_fields = {
            'q': q,
            'title': title,
            'author': author,
            'publisher': publisher,
            'year': year,
            'genre': genre,
            'imdbid': imdbid,
            'tmdbid': tmdbid
        }
        # Run sql building 
        sql_query, query_params = self.sql_building(optional_fields)
        # Return a consulting.
        return self.run_consulting(sql_query, query_params)

    def sql_building(self, optional_fields: dict):
        # Building the values of Where and Clauses, for each optional parameter that is not None.
        where_clauses = []
        where_values = []
        for field, value in optional_fields.items():
            if value is None:
                continue
            where_clauses.append(f'{field} LIKE ?')
            where_values.append(f'%{value}%')
        
        # Construct the SQL query.
        sql_query = 'SELECT * FROM tv_show tv_show WHERE q LIKE ?'
        
        if where_clauses:
            sql_query += ' AND ' + ' AND '.join(where_clauses)
        
        # Construct the query params.
        query_params = tuple([f'%{optional_fields["q"]}%'] + where_values)

        return (sql_query, query_params)

    def run_consulting(self, sql_query, query_params):
        self.cursor.execute(sql_query, query_params)
        return self.cursor.fetchall()


if __name__ == '__main__':
    from rich.console import Console
    from faker import Faker
    
    console = Console()
    db = MyDataBase()
    
    db.create_table_tv_show()
    console.log('Created table tv_show')
    db.create_table_movie()
    console.log('Created table movie')
    db.create_table_music()
    console.log('Created table music')
    db.create_table_book()
    console.log('Created table book')
    
    base_faker = {
        'q': Faker().word(),
        'season': Faker().word(),
    }
    db.add_tv_show(
        Faker().word(),
        
    )
    