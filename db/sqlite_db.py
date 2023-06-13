import sqlite3 as sq

db = sq.connect('botopizza.db')
cur = db.cursor()


def start_db():
    if db:
        print('DB connected successfully')
    db.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    db.commit()


async def add_to_db(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
        db.commit()
