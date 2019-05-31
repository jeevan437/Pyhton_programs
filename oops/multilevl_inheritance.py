class A:
    def one(self):
        print("func one from class A")

    def two(self):
        print("func two from class A")

class B(A):
    def three(self):
        print("func three from class B")

class C(B):
    def four(self):
        print("func four from class C")

obj = C()
obj.three()