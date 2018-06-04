import sqlite3
import json

connection = sqlite3.connect("testdb.db")
c = connection.cursor()

def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS foo(id int primary key )")
    c.execute("CREATE TABLE IF NOT EXISTS myorder("
              "      orderId int primary key , itemID VARCHAR(20),"
              "      price decimal,"
              "      quantity int,"
              "      description text)")

def insertData(data):
    result = c.execute("""
      INSERT INTO myorder(orderId, itemId, price, quantity, description) values(?, ?, ?, ?, ?)
    """, data)

if __name__ == '__main__':
    orders = []
    for i in range(1000):
        order = (i, 'Item', 1, 1, 'URGENT' if i % 3 == 0 else ' ')
        orders.append(order)


    createTable()
    for item in orders:
        insertData(item)

    c.execute("select count(*) from myorder")
    print(c.fetchone())
    c.execute("select count(*) from myorder where description=?", ['URGENT'])
    print(c.fetchone())
    c.execute("select count(*) from myorder where description!=?", ['URGENT'])
    print(c.fetchone())
    c.close()