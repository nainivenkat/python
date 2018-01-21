import datetime
from datetime import date
from math import pi
import os.path
import os
import platform
import glob
from subprocess import call

def currentdatetime():
    now =datetime.datetime.now()
    print ("current date time: ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def areaofcircle():
    r = float(raw_input("Enter radius of circle: "))
    print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

def printreverse():
    first = raw_input("Enter first name: ")
    last = raw_input("Enter last name: ")
    print last + " " + first

def listtuple():
    string = raw_input("Input some comma seprated numbers : ")
    print string
    list = string.split(",")
    tuple1 = tuple(list)
    print 'List : ',list
    print 'Tuple : ',tuple1

def listexample():
    color_list = ["Red", "Green", "White", "Black"]
    len1 = len(color_list)
    print color_list[0] +" "+ color_list[len1-1]

def palidrome():
    string = raw_input("Enter the string: ")
    len1 = len(string)
    flag = 1
    for index in range(len1):
        if (string[index] != string[len1-1]):
            flag = 0
            break
        len1 = len1-1
    if (flag):
        print "string is a palindrome"
    else:
        print "string is not a palindrome"

def sample():
    a = 5
    n1 = int( "%s" % a )
    n2 = int( "%s%s" % (a,a) )
    n3 = int( "%s%s%s" % (a,a,a) )
    print (n1+n2+n3)
    """
    num = int(raw_input("Enter number:"))
    if (num <=17):
        print 17 - num
    else:
        print 2* abs(17 - num)
    
    string =str(raw_input("Enter a string:"))
    if len(string)>=2 and (string[:2] == 'Is'):
        print string
    else:
        print 'Is' + string
    
    num = int(raw_input("enter a number:"))
    if (num %2 ==0):
        print "Even number"
    else:
        print "Odd number"
    
    string = str(raw_input("enter comma seperated numbers"))
    list1 = string.split(",")
    count =0
    for index in range(len(list1)):
        if list1[index] == '4':
            count = count+1
    print count
    """
    list1 = ["v","e","n","k","a","t"]
    
    for value in list1:
        print value

        
def deltadays():
    f_date = date(2017, 6, 20)
    l_date = date(2017, 6, 25)
    delta = l_date - f_date
    print delta.days

def volumeofsphere():
    r = float(raw_input("Enter radius: "))
    print ("The volume of the sphere with radius " + str(r) + " is: " + str(4.0/3.0 * pi* r**3))

def listcomprehensions():
    list1 = ["White", "Black", "Red"]
    list2 = ["Red", "Green"]
    print [element for element in list1 if element not in list2]

def areaoftriange(list):
    area = list[0]*list[1]/2
    return area

def sumofthree(list):
    value = list[0] + list[1] 
    if value >=15 and value <=20:
        return 20
    return value

def osconcepts():
    open('abc.txt', 'w')
    print (os.path.isfile('C:\Naini\python_scripts\excercises\os_concepts.py'))
    print(os.path.isdir('C:\Naini\python_scripts\excercises'))
    print(os.name)
    print(os.path.abspath('venkat.txt'))
    print(platform.system())
    print(platform.release())
    #print(call(["ls", "-l"]))
    print ('current file name :', os.path.realpath(__file__))
    #print (os.environ['PATH'])

def highestnumber(n, string):
    char = n
    count =0
    for element in string:
        if n == element:
            count = count +1
    print 'number of occurrences of,', n ,'is:', count, '\n'
    print string.count('v')
'''
    length = list.len()
    if (n > list[length-1]):
        print True
    else:
        print False

    for element in list:
        if n > element:
            print True
        else:
            print False
'''
def swap(list):
    temp =list[0]
    list[0] = list[1]
    list[1] = temp
    return list
def listoffiles():
    
    file_list = glob.glob('*.*')
    print file_list
if __name__ == '__main__':
    #currentdatetime()
    #areaofcircle()
    #printreverse()
    #listtuple()
    #listexample()
    #palidrome()
    #sample()
    #deltadays()
    #volumeofsphere()
    #listcomprehensions()
    #print(areaoftriange([20,40]))
    #print(sumofthree([15,3]))
    #osconcepts()
    #highestnumber('a','venkata')
   # print swap([5,6])
    listoffiles()
    

