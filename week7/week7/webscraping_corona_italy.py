import bs4
import requests
import matplotlib.pyplot as plt
import numpy as np

#Brug webscraping til at hente antallet af samlet antale corona cases, døde og overlevende/raske

r = requests.get("https://www.worldometers.info/coronavirus/country/italy/")

r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

elements = soup.select('div[id] span')

for element in elements:
    print(element.getText())

# Lav et bar char over samlet antal corona cases. døde og overlevende/raske 

objects = ('Infected', 'Dead', 'Recovered')
y_pos = np.arange(len(objects))
numbers = [15113, 1016, 1258]

plt.bar(y_pos, numbers, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.title('Corona virus in italy 13/03-2020 kl. 11:20')

plt.show()