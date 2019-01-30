class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

class Square:
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len * 4

rect = Rectangle(3, 4)
square = Square(5)
print(rect.calculate_perimeter())
print(square.calculate_perimeter())
