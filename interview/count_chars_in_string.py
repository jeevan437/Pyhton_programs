s = "programming for programmers"

from collections import defaultdict,Counter
# d = defaultdict(int)
d={}
# print(Counter(s))

for i in s:
    d[i] =s.count(i)

print(d)
