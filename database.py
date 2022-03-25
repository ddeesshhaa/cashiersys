import sqlite3
from pathlib import Path

db = sqlite3.connect('mangement.db')  # make database connection


def SetTables():
    db.execute("CREATE TABLE store_data(store_name text,phone text,address text)")
    db.execute("CREATE TABLE users(user_id integer,user_name text,user_pass text,priv integer)")
    db.execute(
        "CREATE TABLE items(item_id integer,name text,quantity integer,price integer)")
    db.execute(
        "CREATE TABLE transition(item_id integer,name text,price integer,quantity integer,money integer,date text)")
    db.execute("INSERT into users(user_id,user_name,user_pass,priv)values(1,'admin','admin',1)")
    db.commit()


def WriteData(order, data):
    db.execute(order, data)
    db.commit()

def DeleteData(order, data):
    db.execute(order, data)
    db.commit()


def ReadData(order):
    cr = db.cursor()
    getData = cr.execute(order)
    data = getData.fetchall()
    return data
