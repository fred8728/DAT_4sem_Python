import pandas as pd
import matplotlib.pyplot as plt

#Use another table 

#Hvor mange mange blev født d 9 december hver 5 år ( FOLK3 ) 

url = 'https://api.statbank.dk/v1/data/FOLK3/CSV?FDAG=D09&FMAANED=012&FODAAR=1970%2C1975%2C1980%2C1985%2C1990%2C1995%2C2000%2C2005%2C2010%2C2015'
data = pd.read_csv(url, sep=';')

plt.figure()
plt.bar(data['FODAAR'], data['INDHOLD'])

# Hvor mange havde dansk statsborgerskab i 2000 vs 2020
url = 'https://api.statbank.dk/v1/data/FOLK2/CSV?STATSB=DANSK%2CUDLAND&Tid=2000%2C2020'
data = pd.read_csv(url, sep=';')
dansk = data[data['STATSB'] == 'Dansk']
udenlandsk = data[data['STATSB'] == 'Udenlandsk']

d = plt.bar(dansk['TID'], dansk['INDHOLD'])
u = plt.bar(udenlandsk['TID'], udenlandsk['INDHOLD'])
plt.legend([u,d], ['Udenlandsk', 'Dansk'], loc=1)
plt.show()