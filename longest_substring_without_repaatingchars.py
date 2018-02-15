string = "geeksforgeeks"
count = 0
list1 = []
list2 = []
max1 = 0

for char in string:
    if char not in list1:
        list1.append(char)
        count += 1
    else:
        if count > max1:
            max1 = count
            list2 = list1
            list1 = []
        count = 0

print list2
