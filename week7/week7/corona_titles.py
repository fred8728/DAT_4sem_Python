import bs4
import requests

#Webscrape alle titlerne, samt antallet af artikler

r = requests.get("https://www.dr.dk/nyheder/tema/coronavirus")

r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

elems = soup.select('div a span span')

for elem in elems:
    print (elem.getText())

print("Number of articles {ele}".format(ele = len(elems)))