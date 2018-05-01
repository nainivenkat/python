list1 =  [-1, 2, -3, 4, 5, 6, -7, 8, 9]

list2 = []
list3 = []

for element in list1:
    if element >0:
        list2.append(element)
    else:
        list3.append(element)

list4 = []

i = j = 0
while i <len(list2) and j < len(list3):
    list4.append(list2[i])
    list4.append(list3[j])
    i = i+1
    j = j+1

while i < len(list2):
    list4.append(list2[i])
    i = i+1
while j < len(list3):
    list4.append(list3[j])
    j = j+1

print list4
    
