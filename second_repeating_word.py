from  operator import itemgetter

string = "aaa bbb ccc aaa bbb aaa"
list1 = string.split()
dict1 = {}

for element in list1:
    if element in dict1.keys():
        dict1[element] += 1
    else:
        dict1[element] = 1

dict1 = sorted(dict1.items(), key= itemgetter(1), reverse = True)
print dict1[1][0]
