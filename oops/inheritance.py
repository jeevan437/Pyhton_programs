class A:
    def hello(self):
        print("hello func from class A")


class B(A):
    def hello(self):
        print("hello func from class B")

obj = B()
obj.hello()