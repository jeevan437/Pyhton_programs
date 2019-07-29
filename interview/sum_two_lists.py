l1 = [1,2,3]
l2 = [4,5,6]

for i in enumerate(l1):
    for j in enumerate(l2):
        if i[0] == j[0]:
            print(i[1]+j[1])