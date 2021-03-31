from .student import Student

class Classroom:
    def __init__(self, students = None):
        if students:
            self.students = students
        else:
            self.students = []
    
    def add_student(self, student):
        self.students.append(student)

    def classroom_count(self):
        return len(self.students)

    