class Apple:
    def __init__(self, c, w, isPC, isPhone):
        self.color = c
        self.weight = w
        self.isPC = isPC
        self.isPhone = isPhone


apple = Apple('red', 100, False, False)
print(apple)
