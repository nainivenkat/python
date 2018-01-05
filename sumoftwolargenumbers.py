def sumoftwonumbers(str1,str2):
    list1 = list(str1)
    list2 = list(str2)
    len1 = len(list1)
    len2 = len(list2)
    diff = abs(len1-len2)
    if len1>len2:
        for i in range(diff):
            list2.insert(i,0)
    else:
        for i in range(diff):
            list1.insert(i,0)
    list1 = list1[::-1]
    list2 = list2[::-1]
    print list1
    print list2
    sum = 0
    carry = 0
    list3 = []
    for i,j in zip(list1,list2):
        
        sum = i+j+carry
        carry = sum //10
        if sum >= 10:
            sum = sum %10

        list3.append(sum)

    if carry:
         list3.append(carry)
    return list3[::-1]

print sumoftwonumbers("7777555511111111", "3332222221111")
