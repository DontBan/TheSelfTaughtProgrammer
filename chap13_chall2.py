class Square:
    def __init__(self, l):
        self.len = l
        
    def change_size(self, l):
        self.len += l

    def calculate_perimeter(self):
        return self.len * 4

square = Square(3)
print(square.calculate_perimeter())
square.change_size(2)
print(square.calculate_perimeter())
