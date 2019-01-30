class Shape:
    def what_am_i(self):
        return 'I am a shape'

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

class Square(Shape):
    def __init__(self, l):
        self.len = l
        
    def change_size(self, l):
        self.len += l

    def calculate_perimeter(self):
        return self.len * 4

rect = Rectangle(4, 3)
square = Square(4)
print(rect.what_am_i())
print(square.what_am_i())
