list1 = [2,1,4,6,7,8,70,69]

list2 = []
for i in range(1,len(list1)):
    if  abs(list1[i]-list1[i-1]) == 1:
        list2.append((list1[i],list1[i-1]))


print list2
