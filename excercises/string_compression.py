def compress(string):
    len1 = len(string)
    i = 1
    count = 1
    r = ""

    if len1 == 0:
        return " "
    if len1 == 1:
        return string+'1'
    
    while i < len1:
        if string[i] == string[i-1]:
            count +=1
        else:
            r = r+string[i-1]+str(count)
            count = 1
        i = i+1
    r = r+string[i-1]+str(count)
    return r

string = "aaabbccccab"
print compress(string)
