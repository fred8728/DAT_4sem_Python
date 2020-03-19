#Create a module containing a class with the following methods:
#init(self, url_list)
#download(url,filename) raises NotFoundException when url returns 404
#multi_download(url_list) uses threads to download multiple urls as text and stores filenames as a property
#iter() returns an iterator
#next() returns the next filename (and stops when there are no more)
#urllist_generator() returns a generator to loop through the urls
#avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
#hardest_read() returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.

import os
import urllib.request as req
from urllib.parse import urlparse
import urllib
import requests
import threading
import re

class module:
    
# 1) init (self, url_list)
    def __init__(self, url_list):
        self.url_list = url_list

# 2) raises NotFoundException when urls returns 404
    def download(self, url, filename=None):
        class NotFoundException(ValueError):
    
                def __init__(self, *args, **kwargs):
                    ValueError.__init__(self, *args, **kwargs) 
        if filename:
            localfile = filename
        else:
            filename = os.path.basename(urlparse(url).path)
            localfile = os.path.join('.', filename)
        
        res = requests.get(url)
        if res.status_code == 404:
            raise NotFoundException('Not found')
        else:
            print('Det viiiirrkeeeer ;D')
            with open(filename, 'wb') as fd:
                for chunk in res.iter_content(chunk_size=1024):
                    fd.write(chunk) 

# 4) returns an iterator
    def __iter__(self):
        return self

# 5) returns the next filename and stops when there is no more
    def __next__(self):
        if len(self.url_list) == 0:
            raise StopIteration()
        else:
            for url in self.url_list:
                filename = os.path.basename(urlparse(url).path)
                with open(filename) as file:
                    print(filename)
                    return filename
            
# 6 returns a generator to loop through the urls
    def urllist_generator(self):
        for url in self.url_list:
            print(url)

# 7) return average number of vowels in the words of a text
    def avg_vowels(self, text):
        with open(text) as file:
            lines = file.readlines()
        vowel_string = ''

        for line in lines:
            vowel_string += line

        words = len(re.findall(r'\w+', vowel_string)) 
        vowels = len(re.findall(r'[aeiou]', vowel_string, flags=re.IGNORECASE))
        print(words/vowels)
        return words/vowels
        