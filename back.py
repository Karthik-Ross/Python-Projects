import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Routine (Id INTEGER PRIMARY KEY, Date TEXT, Earnings INTEGER, Excercise TEXT, Study TEXT, Diet TEXT, Python TEXT)")
    conn.commit()
    conn.close()

def insert(Date, Earnings, Excercise, Study, Diet, Python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Routine VALUES (NULL, ?, ?, ?, ?, ?, ?)", (Date, Earnings, Excercise, Study, Diet, Python))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Routine WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def search(Date='', Earnings='', Excercise='', Study='', Diet='', Python=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Routine WHERE date=? OR Earnings=? OR Excercise=? OR Study=? OR Diet=? OR Python=?", (Date, Earnings, Excercise, Study, Diet, Python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
