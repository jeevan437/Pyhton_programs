#bound and unbound method calls

# class Methods:
#     def __init__(self):
#         self.name = 'Methods'
#
#     def getName(self):
#         return self.name
# m=Methods()
# print(m.getName())
# print(Methods.getName(m))

class Student:

    a=10
    def __init__(self,name,loc):
        self.name = name
        self.loc = loc
    def displayStudent(self):
        print("name:",self.name , "loc:",self.loc)

obj = Student('jeevan','hyd')
obj.displayStudent()