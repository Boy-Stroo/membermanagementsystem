from abc import ABC
import sqlite3

class Service(ABC):
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.table = 'table'
        self.columns = {}

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Service, cls).__new__(cls)
        return cls.instance

    def create_table(self):
    # ID TEXT PRIMARY KEY NOT NULL
    # REST OF THE COLUMNS TEXT
        columns = ', '.join([f"{column} TEXT PRIMARY KEY NOT NULL" if column == 'id' else f"{column} TEXT" for column in self.columns])
        self.c.execute(f'CREATE TABLE IF NOT EXISTS {self.table} ({columns})')
        self.conn.commit()

    def get_all_from_table(self, table, columns):
        self.c.execute(f'SELECT {", ".join(columns)} FROM {table}')
        return self.c.fetchall()
    
    def create_in_table(self, table, columns, data: list):
        self.c.execute(f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({", ".join(["?" for _ in columns])})', (*data,))
        self.conn.commit()
        return self.c.lastrowid
    
    def update_in_table(self, table, columns, data: list, id):
        self.c.execute(f'UPDATE {table} SET {", ".join([f"{column} = ?" for column in columns])} WHERE id = ?', (*data, id))
        self.conn.commit()
        return self.c.rowcount
    
    def delete_from_table(self, table, id):
        # id sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 256 supplied.
        self.c.execute(f'DELETE FROM {table} WHERE id = ?', (id,))
        self.conn.commit()
        return self.c.rowcount
    
    def get_all(self):
        return self.get_all_from_table(self.table, self.columns)

    def create(self, data):
        return self.create_in_table(self.table, self.columns, data)

    def delete(self, id):
        return self.delete_from_table(self.table, id)
    
    def update(self, data, id):
        return self.update_in_table(self.table, self.columns, data, id)