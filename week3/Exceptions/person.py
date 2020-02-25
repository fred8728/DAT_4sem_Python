import string

class Person():

    def __init__(self, name):
        self.name = name

    def check_name(self):
        for char in self.name:
            if char.isdigit():
                raise InvalidArgumentException('Name cant contain number')
        return self.name

        
        