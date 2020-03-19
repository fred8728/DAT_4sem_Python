# dataframe to table
import pandas as pd 
import pymysql
from sqlalchemy import create_engine #sqlalchemy helped convert strings to dates seamlessly

# Create a function that can take a dict and a table name and persist all values of the dict into the table columns corresponding to the dict keys.

con_str = 'mysql+pymysql://dev:ax2@localhost:3307/test'
engine = create_engine(con_str)

df = pd.DataFrame({'make' : ['vw', 'audi', 'citroen'],
                   'model' : ['up', 'a6', 'c2'],
                   'year' : [2018, 2011, 2019],
                   'price' : [12300, 85000, 143000]
    
})
#df = df.applymap(str)
df.to_sql('cars',con=engine, if_exists='append', index = False)
print(df.dtypes)

# Thomas løsning
# csv = """
# make,model,year,price
# vw,up,2018,123000
# audi,a6,2011,85000
# citroen,c3,2019,143000
# """
# data = pd.read_clipboard(sep=",")
# data