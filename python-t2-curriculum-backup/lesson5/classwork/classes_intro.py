class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print("Hi, my name is", self.name)
        print("I am in grade", self.grade)

student1 = Student("Kaiden", 6)
student1.introduce()

student2 = Student("Ben", 10)
student2.introduce()

student2.grade = 12
student2.introduce()