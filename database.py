import sqlite3

def get_connection():
    conn = sqlite3.connect("tarefas.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
        conn = get_connection()
        conn.execute ("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                concluida INTEGER DEFAULT 0
            )
       """ )    
        conn.commit()
        conn.close()
            
