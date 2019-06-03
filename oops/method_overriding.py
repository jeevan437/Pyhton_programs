class A:
    def f1(self):
        print("f1 from A class")

    def f2(self):
        print("f2 from A class")

class B(A):
    def f1(self):
        super(B,self).f1()
        print("f1 from B class")

obj = B()
obj.f1()
obj.f2()
