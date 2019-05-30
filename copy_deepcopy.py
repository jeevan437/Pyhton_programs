# shallow copy
import copy
# l=[2,3,4,5,6]
# print(l)
# l1 = copy.copy(l)
# print(l1)
# l[4] = 7
# print("after shallow copy()")
# print(l)
# print(l1)

m=[2,3,4,5,6]
print(m)
m1=copy.deepcopy(m)
print(m1)
#after deepcopy
print("after deep copy")
m[4] = 7
print(m)
print(m1)