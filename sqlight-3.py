import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('filethrityeight')


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT,value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1234512345, '2016-10-28', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time() # trim this value? Yes
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot(unix, datestamp, keyword, value) VALUES(?,?,?,?)",
              (unix,date,keyword,value))
    conn.commit()

def read_from_db():
#    c.execute("SELECT * FROM stuffToPlot")
#    c.execute("SELECT * FROM stuffToPlot WHERE value = 3 AND keyword = 'Python'")
    c.execute("SELECT * FROM stuffToPlot WHERE unix > 1477483619.641093")

# data = c.fetchall()
    for r in c.fetchall():
        print(r)
        print(r[2]) # get just a column

def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        print(row)


# create_table()
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)
graph_data()
c.close()
conn.close()

