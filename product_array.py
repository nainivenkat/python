list1 = [1,5,0,0]
zero_index = 0
count = 0
product = 1
list2 = []

for index, element in enumerate(list1):
    if element != 0:
        product = product*element
    else:
        count +=1
        zero_index = index


if count == 2:
    list2 = [0 for element in range(len(list1))]
elif count == 1:
    list2 = [0 for element in range(len(list1))]
    list2.insert(index, product)
else:
    for element in list1:
        list2.append(product/element)

print list2



        
