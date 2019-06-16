class Overloading:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.x + self.y

    def __add__(self, other):
        self.other = other

        print(self.x + other.x)
        print(self.y + other.y)

obj = Overloading("python","world")
obj1 = Overloading("java","language")

print(obj + obj1)