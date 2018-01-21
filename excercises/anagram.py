a = 'umbrella'
b = 'aumbllre'

def match_word(a, b):
    a = "".join(sorted(a))
    b = "".join(sorted(b))
    if a == b:
        return True
    else:
        return False


print match_word(a,b)

