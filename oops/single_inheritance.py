class Parent:
    def func(self,x,y):
        self.x=x; self.y = y
        c = self.x + self.y
        print("iam in func of parent class:",c)

    def hello(self):
        self.x = 30
        self.y = 40
        print("hello", self.x + self.y)

class child(Parent):
    print("im in child class")
    # print("Derived class:", )
obj = child()
print(obj.func(10,20))
print(obj.hello())