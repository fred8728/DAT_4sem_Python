

class Student():

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        lst = self.data_sheet.get_grades_as_list()
        sum = 0
        for grade in lst:
            sum += grade
        return sum/len(lst)

class DataSheet():

    def __init__ (self, courses):
        self.courses = courses

    def get_grades_as_list(self):
        lst = []
        for course in self.courses:
            if(course.get_grades() != None):
                lst.append(course.get_grades)
                return lst

class Course():
    
    def __init__(self, name, classroom, teacher, ETCS, grade=0 ):
        self.name=name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade

    def get_grades(self):
        return self.grade

    def get_ETCS(self):
        return self.ETCS