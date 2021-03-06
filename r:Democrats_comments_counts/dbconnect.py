#!/usr/bin/python
import psycopg2
from config import config
import datetime
conn = None
def connect():
    """ Connect to the PostgreSQL database server """
    params = config()
    print('Connecting to the PostgreSQL database...')
    global conn
    conn = psycopg2.connect(**params)

def disconnect():
    global conn
    conn.close()
    print('Database connection closed.')

def getdeminfo():
    cur = conn.cursor()
    insert_stmt = (
        "SELECT body from democratcom2020"
        )
    cur.execute(insert_stmt)
    result = cur.fetchall()
    cur.close()
    return result


def main():
    connect()
    disconnect()
if __name__ == '__main__':
    main()
