class Class :
    def add(self,x,y):
        return x+y

obj = Class()

def not_add(self,x,y):
    return x+y+10

Class.add = not_add
print(obj.add(5,6))