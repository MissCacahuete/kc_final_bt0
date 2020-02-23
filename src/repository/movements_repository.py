from domain.movement import Movement
from repository.base_repository import connect, DATABASE


def insert_movement(movement):
    conn = connect(DATABASE)
    c = conn.cursor()
    sql = "INSERT INTO movements (date, time, from_currency, from_quantity, to_currency, to_quantity) VALUES(?,?,?,?,?,?)"
    values = (movement.date, movement.time, movement.from_currency, movement.from_quantity, movement.to_currency,
              movement.to_quantity)
    c.execute(sql, values)
    print('Inserted new movement.')

    conn.commit()

    c.close()
    conn.close()


def list_movements():
    conn = connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM movements")
    movements = []
    for it in c.fetchall():
        movements.append(Movement(it[0], it[1], it[2], it[3], it[4], it[5], it[6]))
    c.close()
    conn.close()

    return movements

def clear_movement():
    conn = connect(DATABASE)
    c = conn.cursor()
    c.execute("DELETE FROM movements")
    print("Todo los registros han sido borrados")
    conn.commit()
    c.close()
    conn.close()
