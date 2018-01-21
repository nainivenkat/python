string = "aabcccccaaa"
count = 0
string1 = ""
for i in range(len(string)):
    count +=1
    if i+1 >= len(string) or string[i] != string[i+1]:
        string1 += ""+string[i]+str(count)
        count = 0
print string1
