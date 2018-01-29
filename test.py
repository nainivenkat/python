import re

def checkpattern(string):
    pattern = '[a-zA-Z]'
    if re.search(pattern,string):
        print True




checkpattern("Venkat")
