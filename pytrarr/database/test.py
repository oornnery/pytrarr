import unittest
import sqlite3
from faker import Faker
from db import MyDataBase  # Substitua "my_database" pelo nome do arquivo onde você definiu a classe MyDataBase

class TestMyDataBase(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.database_path = "pytrarr/database/database.db"  # Use um banco de dados de teste separado
        self.db = MyDataBase()

    def tearDown(self):
        self.db.close()
        # Limpa o banco de dados de teste após cada teste
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS tv_show")
        cursor.execute("DROP TABLE IF EXISTS movie")
        cursor.execute("DROP TABLE IF EXISTS music")
        cursor.execute("DROP TABLE IF EXISTS book")
        conn.commit()
        conn.close()

    def test_create_tables(self):
        # Testa a criação das tabelas
        self.db.create_table_tv_show()
        self.db.create_table_movie()
        self.db.create_table_music()
        self.db.create_table_book()

        # Verifica se as tabelas foram criadas com sucesso
        conn = sqlite3.connect(self.database_path)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(tv_show)")
        tv_show_columns = [column[1] for column in cursor.fetchall()]
        cursor.execute("PRAGMA table_info(movie)")
        movie_columns = [column[1] for column in cursor.fetchall()]
        cursor.execute("PRAGMA table_info(music)")
        music_columns = [column[1] for column in cursor.fetchall()]
        cursor.execute("PRAGMA table_info(book)")
        book_columns = [column[1] for column in cursor.fetchall()]
        conn.close()

        self.assertIn("id", tv_show_columns)
        self.assertIn("id", movie_columns)
        self.assertIn("id", music_columns)
        self.assertIn("id", book_columns)

    def test_add_data(self):
        # Testa a adição de dados fictícios
        self.db.create_table_tv_show()

        # Gera dados fictícios usando o Faker
        q = self.fake.word()
        season = self.fake.word()
        ep = self.fake.word()
        imdbid = self.fake.word()
        tmdbid = self.fake.word()
        year = self.fake.word()
        genre = self.fake.word()
        torrent = self.fake.word()

        # Adiciona os dados fictícios ao banco de dados
        self.db.add_tv_show(q, season, ep, imdbid, tmdbid, year, genre, torrent)

        # Consulta os dados no banco de dados
        result = self.db.search_tv_show(q)
        self.assertEqual(len(result), 1)

        # Verifica se os dados adicionados correspondem aos dados fictícios
        tv_show = result[0]
        self.assertEqual(tv_show[1], q)
        self.assertEqual(tv_show[2], season)
        self.assertEqual(tv_show[3], ep)
        self.assertEqual(tv_show[4], imdbid)
        self.assertEqual(tv_show[5], tmdbid)
        self.assertEqual(tv_show[6], year)
        self.assertEqual(tv_show[7], genre)
        self.assertEqual(tv_show[8], torrent)

if __name__ == "__main__":
    unittest.main()
