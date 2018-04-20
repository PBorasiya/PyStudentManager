students=[]


class Student:

    school_name = "Sanskardeep Vidyalaya"

    def __init__(self, name, student_id=32):
        self.name = name
        self.student_id = student_id
        students.append(self)


    def __str__(self):
        return "" + self.name


    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_schoole_name(self):
        return self.school_name

class HighSchoolStudent(Student):

    school_name = "SVEM"

    def get_schoole_name(self):
        return  "SVEM student"

    def get_name_capitalize(self):
        original_name = super().get_name_capitalize()
        return original_name + "-SVEM"



