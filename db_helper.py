import sqlite3


def create_connection():
    try:
        conn = sqlite3.connect("main.db")
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


def select_challenges(param):
    sql = "SELECT " + param + " FROM challenges"
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute(sql)
        answer = cur.fetchone()[0]
    return answer


def update_challenges(param, val):
    conn = create_connection()
    sql = "UPDATE challenges SET " + param + " = " + val
    cur = conn.cursor()
    cur.execute(sql)
