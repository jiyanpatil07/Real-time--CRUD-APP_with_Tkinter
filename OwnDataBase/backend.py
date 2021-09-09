from os import curdir
import sqlite3 
def connect():
    conn=sqlite3.connect("routine.db")
    cur=conn.cursor()
    cur.execute("create table if not exists routine(id integer primary key ,date text,earning integer,exercise text, study text,diet text, python text)")
    conn.commit()
    conn.close()


def insert(date,earning,exercise,study,diet,python):
    conn=sqlite3.connect("routine.db")
    cur=conn.cursor()
    cur.execute("insert into routine values (null,?,?,?,?,?,?)",(date,earning,exercise,study,diet,python))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("routine.db")
    cur=conn.cursor()
    cur.execute("select * from routine")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("routine.db")
    cur=conn.cursor()
    cur.execute("delete from routine where id=?", (id,))
    conn.commit()
    conn.close()


def search(date="",earning="",exercise="",study="",diet="",python=""):
    conn=sqlite3.connect("routine.db")
    cur=conn.cursor()
    cur.execute("select * from routine where date=? or earning=? or exercise=? or study=? or diet=? or python=?",(date,earning,exercise,study,diet,python))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows


# delete(2)
x= search(date='8-1-2020')
print(x)
# insert('1-1-2020',200,'noexercie','not studyes','diet taker','did python')
# insert('1-1-2020',200,'noexercie','not studyes','diet taker','did python')
# insert('8-1-2020',200,'noexercie','not studyes','diet taker','did python')
# print(view())