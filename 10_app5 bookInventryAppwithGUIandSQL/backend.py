import sqlite3


def connect():
    conn = sqlite3.connect("10_app5 bookInventryAppwithGUIandSQL/books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("10_app5 bookInventryAppwithGUIandSQL/books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("10_app5 bookInventryAppwithGUIandSQL/books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    # conn.commit() 因为这是一个select statement，不对数据库做任何变动，所以不需要这个func
    conn.close()
    return rows


# in case the user only input one parameter, and other will have no value, which will cause error. So put every argument ""
def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("10_app5 bookInventryAppwithGUIandSQL/books.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    # conn.commit() 因为这是一个select statement，不对数据库做任何变动，所以不需要这个func
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("10_app5 bookInventryAppwithGUIandSQL/books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("10_app5 bookInventryAppwithGUIandSQL/books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()


# connect()
# # insert("The Sun", "John Adam", 1288, 6488568486)
# # delete(3)
# update(4, "The Moon", "Jonh Smith", 1999, 999999)
# print(view())
# print(search(author="John Smith"))
