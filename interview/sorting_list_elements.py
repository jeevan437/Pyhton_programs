l=[0,0,1,1,0,1,0,1,1]

# l1 = []
# print(sorted(l))

for i in range(len(l)):
    for j in range(i+1,len(l)):

        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]

print(l)

