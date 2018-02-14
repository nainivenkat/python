from operator import itemgetter

def test1(dict1):
    
    sorted_dict = sorted(dict1.items(), key= itemgetter(1))
    return sorted_dict



if __name__ == '__main__':
    print test1({0:10, 1:30, 2:50, 3:20})
