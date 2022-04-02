import sqlite3
from sqlite3 import Connection
class DB:
    def __init__(self) -> Connection:
        self.conn = sqlite3.connect('./db/passwords.db', check_same_thread=False)
        self.cur = self.conn.cursor()
        self.execsql('CREATE TABLE IF NOT EXISTS psd(pass TEXT NOT NULL)')
    
    def execsql(self, query: str, entities: tuple=None) -> None:
        if not entities:
            self.cur.execute(query)
        else:
            self.cur.execute(query, entities)
        self.conn.commit()

    def read_data(self) -> list[tuple, tuple, tuple]:
        result = self.cur.execute("SELECT * FROM psd")
        res = result.fetchall()
        return res

    def check_db(self, password: str) -> bool:
        res = self.read_data()
        s = [pwd[0] for pwd in res if pwd[0] == password]
        if s:
            return True
        return False
    
    def store(self, password: str) -> None:
        return self.execsql("INSERT INTO psd(pass) VALUES(?)", (password,))