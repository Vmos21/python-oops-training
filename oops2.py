class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Vector({self.x:.2f}, {self.y:.2f})"
    def __repr__(self):
        return f"Vector(x = {self.x:.2f} , y = {self.y:.2f})"

v = Vector(2.0, 5.0)
print(v)
print(repr(v))