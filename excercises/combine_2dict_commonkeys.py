from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d3 = {}
for key1, value1 in d1.items():
    for key2, value2 in d2.items():
        if key1 == key2:
            d3[key1] = value1+ value2
        elif key1 not in d3.keys() and key1 not in d2.keys():
            d3[key1] = value1
        elif key2 not in d3.keys() and key2 not in d1.keys():
            d3[key2] = value2
print d3

d4 = {}
d4 = Counter(d1) + Counter(d2)
print dict(d4)
