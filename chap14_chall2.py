class Square:
    square_list = []

    def __init__(self, l):
        self.l = l
        self.square_list.append(self)

    def __repr__(self):
        return '{} by {} by {} by {}'.format(self.l, self.l, self.l, self.l)

s1 = Square(5)
s2 = Square(3)
s3 = Square(4)


print(Square.square_list)
