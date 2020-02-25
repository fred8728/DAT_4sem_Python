
def list_of_students(lst):
    if(len(lst) <3):
        raise NotEnoughStudentsException('Errororor')
    else:
        return lst



class NotEnoughStudentsException(ValueError):
    
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)

    def studentList(self):
        lst = []
        if(len(self.lst) < 3 ):
            raise NotEnoughStudentsException
        else:
            return lst   


l1 = ['Hans', 'Grethe', 'Malen', 'fds']
l2 = ['Hans', 'Grethe']
print(list_of_students(l1))
print(list_of_students(l2))