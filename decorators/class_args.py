class Decorator:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __call__(self, func, *args):
        def abc(m,n):
            if m>0 and n>0:
                print(func(m,n))

            else:
                print("m and n should be greater than 0")

        return abc

@Decorator(10,20)
def add(a,b):
    return a+b

out = add(22,22)
