from connection import conn,cur
import mysql.connector

try:
    query = "DELETE FROM sessions WHERE TIMESTAMPDIFF(MINUTE,time,CURRENT_TIMESTAMP()) > 30"

    cur.execute(query)
    conn.commit()
    print("cleaned")
except mysql.connector.Error as    e:
    print("db error")
    print(e)