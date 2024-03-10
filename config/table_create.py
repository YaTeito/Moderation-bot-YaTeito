import sqlite3

def tablecreate():
    with sqlite3.connect("server.db") as db:
        cur = db.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS admins(
            id INT,
            verefy INT DEFAULT 0,
            points INT DEFAULT 0
        )""")

        cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id INT,
            balance BIGINT,
            voice_time INTEGER,
            status TEXT, 
            roles_num INT
        )""")

        cur.execute("""CREATE TABLE IF NOT EXISTS warn(
            id INT,
            adm INT,
            reason TEXT,
            date TEXT
        )""")