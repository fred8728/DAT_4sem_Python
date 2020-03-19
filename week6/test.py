import myModule

# url-list 
url_list = [
    'http://www.gutenberg.org/files/12345/12345.txt',
    'http://www.gutenberg.org/files/12346/12346.txt',
    'http://www.gutenberg.org/files/12347/12347.txt',
    'http://www.gutenberg.org/files/12348/12348.txt'
]

lst = myModule.module(url_list)

# 2) download method
# lst.download('http://www.gutenberg.org/files/12345/12345.txt')
# lst.download('http://www.gutenberg.org/files/12346/12346.txt')
# lst.download('http://www.gutenberg.org/files/12347/12347.txt')
# lst.download('http://www.gutenberg.org/files/12348/12348.txt')

# 4 __iter__
# lst.__iter__()

# 5) __next__ method
# lst.__next__()

# 6) urllist_generator method
# lst.urllist_generator()

# 7) avg vowels method
# lst.avg_vowels('12348.txt')
