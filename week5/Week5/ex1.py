import pandas as pd
import matplotlib.pyplot as plt

#a) What is the change in pct of divorced danes from 2008 to 2020?
url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?Tid=2008K1%2C2020K1&CIVILSTAND=TOT%2CF'
data = pd.read_csv(url,sep=';')
pct2008 = data['INDHOLD'][0]/data['INDHOLD'][1]
pct2020 = data['INDHOLD'][2]/data['INDHOLD'][3]
pct_increase = (pct2020/pct2008 * 100)-100
print('The pct of divorced people are increased by {} from 2008 to 2020'.format(pct_increase))


#b) Which of the 5 biggest cities has the highest percentage of 'Never Married'?
url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=2020K1&CIVILSTAND=TOT%2CU&K%C3%98N=TOT&OMR%C3%85DE=101%2C851%2C561%2C461%2C751&ALDER=IALT'
data = pd.read_csv(url, sep=';')
#not_married_pct = {data['OMRÅDE'][not_married][4:]:data['INDHOLD'][not_married]/data['INDHOLD'][all_people]*100 for not_married, all_people in zip(range(5,10),range(0,5))}
result = {}
for not_married, all_people in zip(range(5,10),range(0,5)):
    pct_not_married = data['INDHOLD'][not_married]/data['INDHOLD'][all_people]*100
    city = data['OMRÅDE'][not_married][4:]
    result[city] = pct_not_married
#sorted(not_married_pct,key=not_married_pct.get, reverse=True)
#Copenhagen has the highest percentage of 'never married'

#c) Show a bar chart of changes in marrital status from 2008 till now
import matplotlib.pyplot as plt

url ='https://api.statbank.dk/v1/data/FOLK1A/CSV?CIVILSTAND=F%2CE%2CG%2CU&Tid=2008K1%2C2009K1%2C2010K1%2C2011K1%2C2012K1%2C2013K1%2C2014K1%2C2015K1%2C2016K1%2C2017K1%2C2018K1%2C2019K1%2C2020K1&OMR%C3%85DE=101'
data = pd.read_csv(url, sep=';')
fraskilt = data[data['CIVILSTAND'] == 'Fraskilt']
enke = data[data['CIVILSTAND'] == 'Enke/enkemand']
gift_sep = data[data['CIVILSTAND'] == 'Gift/separeret']
ugift = data[data['CIVILSTAND'] == 'Ugift']
result = fraskilt, enke, gift_sep, ugift

#Plot that shows the change in marrital status
plt.figure()
m1 = plt.bar(fraskilt['TID'], fraskilt['INDHOLD'])
m2 = plt.bar(enke['TID'], enke['INDHOLD'])
m3 = plt.bar(gift_sep['TID'], gift_sep['INDHOLD'])
m4 = plt.bar(ugift['TID'], ugift['INDHOLD'])

#d) Show a bar chart of 'Married' and 'Never Married' for all ages in DK
url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?ALDER=IALT&CIVILSTAND=U%2CG&OMR%C3%85DE=000'
data = pd.read_csv(url, sep=';')
never_married = data[data['CIVILSTAND'] == 'Ugift']
married = data[data['CIVILSTAND'] == 'Gift/separeret']

#plot
plt.figure()
m1 = plt.bar(never_married['CIVILSTAND'], never_married['INDHOLD'])
m2 = plt.bar(married['CIVILSTAND'], married['INDHOLD'])
plt.show()