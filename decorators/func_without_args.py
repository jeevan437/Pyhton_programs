def decorator(func):

    def abc(x,y):
        if x>0 and y>0:
            print(func(x,y))

        else:
            print("x and y should be grater than 0")

    return abc

@decorator
def add(a,b):
    return a+b

out = add(3,4)