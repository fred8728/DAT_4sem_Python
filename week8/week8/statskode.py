import pandas as pd 
from sqlalchemy import create_engine

# Anvend filen 'befkbhalderstatkode.csv'
# Lav denne fil om til en mysql table med navnet statskode 

con_str = 'mysql+pymysql://dev:ax2@localhost:3307/test'
engine = create_engine(con_str)

csv = pd.read_csv('befkbhalderstatkode.csv')
csv.to_sql('statskode',con=engine, if_exists='append', index = False)