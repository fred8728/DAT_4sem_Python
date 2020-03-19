import datetime
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='Bank')  

cursor = cnx.cursor()
query = ("SELECT ID, ACCOUNTNUMBER, BALANCE, CUSTOMERRANKING, FIRSTNAME FROM BANKCUSTOMER")

cursor.execute(query)
for (id, accountnumber, balance, customerranking, firstname) in cursor:
  print(id, accountnumber, balance, customerranking, firstname)
cursor.close()
cnx.close()