# l=[2,2,3,4,10,5,6,7,8]
# # for i in enumerate(l):
# #     print(i,end='')
#
# print(l[0:0])

# print([i for n,i in enumerate(l) if i not in l[:n]])

l1 = [1,2,3,4]
l2 = ['one','two','three']
l3=[]
for i in enumerate(l1):
    for j in enumerate(l2):
        if i[0]==j[0]:
            l3.append((i[1],j[1]))

print(l3)
# print(list(zip(l1,l2)))