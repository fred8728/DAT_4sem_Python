from textcontainer import TextContainer

txt = ('Hej med dig')
container = TextContainer(txt)


print('words:', container.count())
print('Chars:', container.countChars())
print('Letters:', container.countLetters())
print('Remove punc:', container.removePunc())