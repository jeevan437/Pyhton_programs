class Decorator:

    def __init__(self,func):
        self.func = func

    def __call__(self, x, y):

        if y>0:
            print(self.func(x,y))

        else:
            print("y should be greater than 0")

@Decorator
def mul(x,y):
    return x/y

out = mul(10,0)