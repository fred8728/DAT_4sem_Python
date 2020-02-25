import string

class TextContainer():

    def __init__(self, word):
        self.word = word

    def count(self):
        return len(self.word.split(" "))
    def countChars(self):
        return len(self.word)

    def countLetters(self):
        count = 0
        for char in self.word:
            if char in string.ascii_letters:
                count += 1
        return count
    
    def removePunc(self):
        for char in self.word:
            if char in string.punctuation:
                print(char)
                self.word = self.word.replace(char, ' ')
            return self.word