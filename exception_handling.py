def f1(a):
    try:
        a=10/2
        print(a)
    except:
        print("zero dision errror")

    else:
        print("else block")

    finally:
        print("finally block")

f1(5)