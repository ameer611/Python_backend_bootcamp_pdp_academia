class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __str__(self):
        return f"x = {self.x}, y = {self.y}"

v1 = Vector(3, 4)
v2 = Vector(2, 4)

v3 = v1 - v2
print(v3)