import mysql.connector
import os

from mysql.connector import errorcode

def openConnection():
    db_connection = mysql.connector.connect(
        host=os.getenv('MYSQL_LOCAL'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSSQL_PASSWORD'), 
        database=os.getenv('MYSQL_DATABASE'))
    
    return db_connection

def dataExecute(sql):
    db_connection = openConnection()
    cursor = db_connection.cursor()
    cursor.execute(sql)
    rowcount = cursor.rowcount
    close(db_connection)
    
    return rowcount


def dataReturn(sql):
    db_connection = openConnection()
    cursor = db_connection.cursor()
    dados = cursor.execute(sql)
    close(db_connection)

    return dados

def close(db_connection):
    db_connection.close()



