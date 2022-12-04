import sqlite3
DATABASE_NAME = "libros.db"


def libro():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create():
    tables = [
        """CREATE TABLE IF NOT EXISTS LIBROS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
				autor REAL NOT NULL,
				precio INTEGER NOT NULL
            )
            """
    ]
    db = libro()
    cursor = db.cursor()
    for tabla in tables:
        cursor.execute(tabla)
        
        