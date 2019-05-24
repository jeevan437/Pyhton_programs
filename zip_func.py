l1=[1,2,3]
l2 = ['one','two','three']
l3 = []
for i in enumerate(l1):
    for j in enumerate(l2):
        if i[0]==j[0]:
            l3.append((i[1],j[1]))

print(l3)