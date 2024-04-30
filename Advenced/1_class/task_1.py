class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def about(self):
        return f"Meni ismim {self.name.title()}, yoshim {self.age}'da, student id raqamim: {self.id}"

amir = Student("amir", 20, 230530)
print(amir.about())