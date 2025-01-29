class Student:
    courses = []
    grades = []
    
    def __str__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age
    
    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
    
