students=[]

class Student:

    school_name = "Sanskaardeep vidyalaya"

    def __init__(self, name , lastname, student_id=32):
        self.name = name
        self.lastname = lastname
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name + " " + self.lastname

    def get_name_capitalize(self):
        return self.get_name_capitalize()

    def get_school_name(self):
        return self.school_name