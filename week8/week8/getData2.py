import datetime
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')  

cursor = cnx.cursor()
lastname = ("SELECT id, firstname, lastname FROM pythondemo WHERE lastname = 'Juhlborg'")

cursor.execute(lastname)

for (id, firstname, lastname) in cursor:
    print(id, firstname, lastname)

cursor.close()
cnx.close()