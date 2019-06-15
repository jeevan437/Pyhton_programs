def decorator(a,b):
    print("decorator func::",a,b)
    def one(func):
        print("func one:",func)

        def two(x,y):
            if x>0 and y>0:
                print(func(x,y))
                print("function two::",x,y)

        return two

    return one

@decorator(3,4)
def add(x,y):
    return x+y

# out = add(10,20)

out = decorator(10,20)
n = out(add)
print(n(5,5))