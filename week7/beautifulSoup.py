# Use BeautifulSoup to extract all titles on all radio programs https://www.dr.dk/radio/programmer

# First find how many pages there are
# Then find all titles on https://www.dr.dk/radio/programmer?side=1

import bs4 #beautiful soup
import requests 

r = requests.get('https://www.dr.dk/radio/programmer')
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

# Find how  many pages there are
titles = soup.select('div[data-pages]')
for title in titles:
    print(title.get('data-pages'))

print('____________________________________________')

r = requests.get('https://www.dr.dk/radio/programmer?=ide=1')
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

# Find all titles
titles = soup.select('li article div h3')
for title in titles:
    print(title.getText())

print('____________________________________________')

