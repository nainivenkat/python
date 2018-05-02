def index_product(list1):
    output = [None]*len(list1)
    product =1
    i = 0

    while i < len(list1):
        output[i] = product
        product = product * list1[i]
        print output[i], product
        i = i+1

    print output
    product =1
    i = len(list1)-1

    while i >=0:
        output[i] = output[i]*product
        product = product*list1[i]
        print output[i], product
        i = i-1

    print output
    return output

list1 = [1,2,3,4]

print index_product(list1)
