import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="alex",
  password="alex"
)

print(mydb)