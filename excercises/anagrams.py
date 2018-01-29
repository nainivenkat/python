def allAnagram(input):

    dict = {}
    for strVal in input:
        key = ''.join(sorted(strVal))
        print key
        if key in dict.keys():
            dict[key].append(strVal)
        else:
            dict[key] = []
            dict[key].append(strVal)
    output = ""
    print dict.items()
    for key,value in dict.iteritems():
        output = output + ' '.join(value) + ' '
    return output
 
# Driver function
if __name__ == "__main__":
    input=['cat', 'dog', 'tac', 'god', 'act']
    print allAnagram(input)
