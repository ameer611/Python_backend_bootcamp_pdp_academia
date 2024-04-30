class Student:
    def __init__(self, ism, familiya):
        self.first_name = ism
        self.last_name = familiya

    @classmethod
    def from_full_name(cls, element: str):
        first_name, last_name = element.split(" ")
        return cls(first_name, last_name)

student = Student.from_full_name('John Smith')
print(student.first_name) # 'John'
print(student.last_name) # 'Smith'
