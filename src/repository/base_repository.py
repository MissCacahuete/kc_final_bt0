import sqlite3
from sqlite3 import Error

DATABASE = 'resources/Database.db'
SCHEMA = 'resources/schema.sql'

def connect(db_file):
    connexion= None
    try:
        connexion = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return connexion


def database_operation (connexion, file_name):
    qry = open(file_name, 'r').read()
    c = connexion.cursor()
    c.executescript(qry)
    connexion.commit()
    c.close()


def init_db():
    conn = connect(DATABASE)
    database_operation(conn, SCHEMA)


if __name__ == "__main__":
    # Rellenar aqui para probar solo este archivo
    pass