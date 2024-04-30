class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

john = Student(name="John", age=21)
bob = Student(name="Bob", age=32)
alice = Student(name="Alice", age=21)


print(john > bob)  # False
print(john < bob)  # True
print(john == alice)  # True chiqishi kerak