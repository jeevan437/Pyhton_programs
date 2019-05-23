#map(<function object>,<iterable>)
from functools import reduce
l=[2,3,4,5,6,7]
print(list(map(lambda x:x**2, l)))
print(list(map(lambda x:x%2==0, l)))
def squares(x):
    return x**2

# print(squares(5))

print(list(map(squares , [2,3,4,5])))

print(list(filter(lambda x:x%2==0, l)))

d=["hello","python","web services","ruby-on-rails","java"]
print(list(map(lambda x:(x,len(x)),d)))

#reduce

# m = [1, 2, 3, 4]
def do_sum(x1, x2):
    return x1 + x2

print(reduce(do_sum, [10,20,30]))

print(reduce(lambda x,y:x+y,[10,20,30,40]))

print(reduce(lambda x,y:x+y,range(1,5)))