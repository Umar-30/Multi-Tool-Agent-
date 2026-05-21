import sqlite3

def check_db():
    conn = sqlite3.connect("agent.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM searches")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    check_db()
