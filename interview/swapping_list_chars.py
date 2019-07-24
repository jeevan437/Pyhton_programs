l = ["abc","xyz"]
# ["abz","xyc]

l1 = l[0]
l2 = l[1]
s1 = l1.replace('c','z')
s2 = l2.replace('z','c')
print(list((s1,s2)))

