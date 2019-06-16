class Error(Exception):
    #Exception is the base class for all other erros
    pass

class ValueTooSmallError(Error):
    # Raised when the input value is too small"
    pass

class ValueToolargeError(Error):
    #Raised when the input value is too large
    pass


number =10
n = int(input("enter n value::"))
try:
    if n < number :
        raise ValueTooSmallError
    elif n > number:
        raise ValueToolargeError
    else :
        print("the given input matches the number")


except ValueTooSmallError:
    print("This value is too small, try again")

except ValueToolargeError:
    print("This value is too large, Try again")

print("congrtes you guessed it correctly..")