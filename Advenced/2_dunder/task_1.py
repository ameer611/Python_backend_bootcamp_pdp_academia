class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def __str__(self):
        return f"Meni ismim {self.name.title()}."

amir = Student("amir", 20, 230530)
print(amir)