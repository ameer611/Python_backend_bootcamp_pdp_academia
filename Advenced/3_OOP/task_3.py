class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def login(self):
        print(f"{self.name} User Login")
        pass

    def logout(self):
        print(f"{self.name} User Logout")
        pass

class Teacher(User):
    def login(self):
        print(f"{self.name} teacher Login")
    pass

    def logout(self):
        print(f"{self.name} teacher Logout")
    pass

class Mentor(Teacher):
    pass

class Assistant(Teacher):
    pass
