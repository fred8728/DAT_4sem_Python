import datetime
import pymysql

# 

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')  

cursor = cnx.cursor()

salary = ("SELECT  firstname, lastname, salary FROM pythondemo WHERE salary > 50000")

cursor.execute(salary)

for (firstname, lastname, salary) in cursor:
    print(firstname, lastname, salary)

cursor.close()
cnx.close()