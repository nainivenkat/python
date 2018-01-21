start = 50
end = 100
results = []

for i in range(start + 1, end):
    t =str(i)
    if i >10:
        if len(set(t)) != 1:
            list1.append(i)
    else:
        list1.append(i)

print 'Results:', results
