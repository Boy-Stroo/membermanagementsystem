import sqlite3

class Service:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.columns = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Service, cls).__new__(cls)
        return cls.instance


    def get_all_from_table(self, table, columns):
        self.c.execute(f'SELECT {", ".join(columns)} FROM {table}')
        return self.c.fetchall()
    
    def get_by_id_from_table(self, table, columns, id):
        self.c.execute(f'SELECT {", ".join(columns)} FROM {table} WHERE id = ?', (id,))
        return self.c.fetchone()
    
    def create_in_table(self, table, columns, data):
        self.c.execute(f'INSERT INTO {table} ({", ".join(columns)}) VALUES ({", ".join(["?" for _ in columns])})', tuple(data.values()))
        self.conn.commit()
        return self.c.lastrowid
    
    def update_in_table(self, table, columns, id, data):
        self.c.execute(f'UPDATE {table} SET {", ".join([f"{column} = ?" for column in columns])} WHERE id = ?', (*data.values(), id))
        self.conn.commit()
        return self.c.rowcount
    
    def delete_from_table(self, table, id):
        self.c.execute(f'DELETE FROM {table} WHERE id = ?', (id,))
        self.conn.commit()
        return self.c.rowcount
    
    def get_all(self):
        return self.get_all_from_table(self.table, self.columns)

    def get_by_id(self, id):
        return self.get_by_id_from_table(self.table, self.columns, id)

    def create(self, data):
        return self.create_in_table(self.table, self.columns, data)

    def update(self, id, data):
        return self.update_in_table(self.table, self.columns, id, data)

    def delete(self, id):
        return self.delete_from_table(self.table, id)