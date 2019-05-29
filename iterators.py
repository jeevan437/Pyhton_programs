#iterable : An iterable is an object that can be iterated by an iterator
#Iteration : Process of iterating(looping) over the iterable objects
#Iterator : process of creating an iter object from itrable
a=[1,2,3,4,5]
c=iter(a)
print(list(c))
for i in a:
    b=iter(a)

print(b.__next__())
print(list(b))