b=10
print("global scope")
def a(x):
    global c
    # print(c)
    c = "hello welcome to python"
    print("local scope")
    print(b+x)

print(c)
a(5)

def f():
    global s
    print(s)
    s="Look for python programming"
print(s)

#global scope
s="python is great"
f()
print(s)

# use of global keyword

def foo():
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


foo()
# print("x in main : ", x)