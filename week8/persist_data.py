import pymysql
import datetime

#Create a function that can take a dict and a table name and persist all values of the dict into the table columns corresponding to the dict keys.

cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test') 
frederikke = {'firstname':'Frederikke', 'lastname':'Nilsson', 'startdate': '1995-12-09', 'enddate': '2020-02-14', 'salary': '20000000'}

def persist_data(connector, dictionary, tablename):
    columns = ', '.join(dictionary.keys())
    values = tuple(dictionary.values())
    query = 'INSERT INTO {tablename} ({cols}) values ({vals})'.format(tablename=tablename, cols=columns, vals=values)
    cursor = connector.cursor()
    cursor.execute(query)
    id = cursor.lastrowid
    connector.commit()
    cursor.close()
    return id

persist_data(cnx, frederikke, 'pythondemo')