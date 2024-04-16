import mysql.connector as mysql
import json 
from mysql.connector import Error

conn  = mysql.connect(host='localhost',database='coins', user='root',password='')
cursor = conn.cursor( buffered=True , dictionary=True)

def selectUserData(user):

    # Create a new record
    cursor.execute("SELECT * FROM users where id = 2")
    # Fetch all rows
    records = cursor.fetchone()
    
    cursor.close()

    return records

def insertPlayers(chaves,valores):

    sql_insert_query = f"INSERT INTO players ({chaves}) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(sql_insert_query, valores)

def selectLastPlayers():

    cursor = conn.cursor( buffered=True , dictionary=True)
    
    cursor.execute("SELECT * FROM players LIMIT 4")
    # Fetch all rows
    records = cursor.fetchall()

    print(records)

    cursor.close()

    return records

