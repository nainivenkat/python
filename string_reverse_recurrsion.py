def stringreverse(string):
    if len(string) == 1:
        return string
    
    return stringreverse(string[1:])+ string[0]

            

string = "venkat"
print stringreverse(string)
