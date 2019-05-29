def hello():
    print("iam in hello func()")

    for i in range(10):
        yield i

a = hello()
print(list(a))


