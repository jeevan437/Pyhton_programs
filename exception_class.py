a=int(input("enter a value:"))
b=int(input("enter b value::"))
try:
    c=a/b
    print(c)
except Exception as e:
# except ZeroDivisionError:
    print("Denominator must be greater than 0")

    print(type(e).__name__)

else:
    print("no exception")

finally:
    print("closing all the connectios")