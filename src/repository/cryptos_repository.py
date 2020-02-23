from domain.crypto import Crypto
from repository.base_repository import connect, DATABASE


def get_cryptos():
    conn=connect(DATABASE)
    c=conn.cursor()
    c.execute("SELECT name, symbol FROM cryptos")
    cryptos=[Crypto(None, item[0], item[1]) for item in c.fetchall()]
    c.close()
    conn.close()
    return cryptos

def is_cyptos_populated():
    return len(get_cryptos()) <= 0

def insert_cryptos(cryptonedas):
    conn=connect(DATABASE)
    c=conn.cursor()
    sql="INSERT INTO cryptos (id,name,symbol) VALUES(?,?,?)"
    values=[]
    for a in cryptonedas:
        values.append((a.id, a.name, a.symbol))
    values.append((0,'Euro','EUR'))
    c.executemany(sql,values)
    print('We have inserted', c.rowcount, 'records to the table.')

    conn.commit()

    c.close()
    conn.close()
