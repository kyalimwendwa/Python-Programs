import mysql.connector
con=mysql.connector.connect(database="user",user="alex",password="alex",host="127.0.0.1",port='3300')
con.autocommit=True
cursor=con.cursor()
sql="select * from userdetails"
cursor.execute(sql)
result=cursor.fetchall();
print(result)
con.close()
