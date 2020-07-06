import datetime
import pymysql

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test')  

cursor = cnx.cursor()
query = ("SELECT aar, bydel, alder, statkode, personer FROM statskode")

cursor.execute(query)

for (aar, bydel, alder, statkode, personer) in cursor:
    print(aar, bydel, alder, statkode, personer)

cursor.close()
cnx.close()