class A:
    def hello(self,*args):
        print("hello():",args)

obj = A()
obj.hello(10,20,30,40)