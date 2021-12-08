import os
import mysql.connector

conn = mysql.connector.connect(user=os.environ["DbUser"], 
                                  password= os.environ["DbPass"],
                                  host=os.environ["DbHost"],
                                  database=os.environ["DB"])

cur = conn.cursor()

