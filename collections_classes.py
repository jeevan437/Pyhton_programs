# from collections import Counter
#
# l=[2,2,2,2,3,4,4,5,6,7,7,8]
# b=Counter(l)
# print(b)
#
# d={}
# for i in l:
#     d[i] = l.count(i)
#
# print(d)


# from collections import OrderedDict as od
# # #
# # # d= od()
# # # d[1]='one'
# # # d[2] = 'two'
# # # d[3] = 'three'
# # #
# # # # print(d)
# # # for i in d.items():
# # #     print(i)

from collections import defaultdict

# s = 'mississippi'
# d = defaultdict(int)
# for i in s:
#     d[i] +=1
#
# print(d.items())
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
#
# d = defaultdict(list)
# for k,v in s:
#     d[k].append(v)

# print(d.items())


s = "jeevan kumar"
m = s.split()
d = defaultdict(int)

for i in m:
    d[i] +=1

print(d)
