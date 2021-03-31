class Student:
    print("hello")

    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, class_name):
        if class_name in self.classes:
            raise Exception
            
        self.classes.append(class_name)
    

    # quinn = Student(
    #             "Quinn",  # Name
    #             "junior", # Grade
    #             [         # classes
    #                 "Pre-Calc", 
    #                 "English III", 
    #                 "World History", 
    #                 "Gym", 
    #                 "Chemistry", 
    #                 "Music Composition"
    #             ]
    #         )
