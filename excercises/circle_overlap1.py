import math
'''
Method to identify overlapping circles from the two input circles provided as input 
'''
def overlap_any(circle1,circle2):
    x1,y1,r1 = circle1
    x2,y2,r2 = circle2
    base = abs(x1-x2)
    height = abs(y1-y2)
    distance = math.sqrt(base**2 + height**2)

    if distance <= (r1 + r2):
        return circle1, circle2
    else:
        return (0,0,0)
'''
Method to create a key lambda function to sort of largest radius circle
'''
def getkey(tuple1):
    return tuple1[2]

'''
Method to take list of arguments as circles and remove overlapping circles. 
'''
def cricle_cluster(*args):
    circles = []
    remove_circles = []
    sorted_circles = []
    output_circles = []

    # Since the input arguments can be any number, *args let us provide dynamic input. Function populates circles list
    for circle in args:
        circles.append(circle)
    sorted_circles = sorted(circles, key = getkey, reverse=True)
    
  
    for i in range(len(sorted_circles)):
        if i+1 < len(sorted_circles):
            overlap_circle = overlap_any(sorted_circles[i], sorted_circles[i+1])
            if overlap_circle:
                for element in overlap_circle:
                    remove_circles.append(element)
    
    for output_circle in sorted_circles:
        if output_circle not in remove_circles:
            output_circles.append(output_circle)
    print remove_circles
    print output_circles
   # return output_circles

'''
c1 = (0.5,0.5,0.5)
c2 = (1.5,1.5,1.1)
c3 = (0.7,0.7,0.4)
c4 = (4,4,0.7)

c1 = (1.5,1.5,1.3)
c2 = (4,4,.07)

c1 = (1,3,0.7)
c2 = (2,3,0.4)
c3 = (3,3,0.9)
'''
c1 = (0.5,0.5,0.5)
c2 = (1.5,1.5,1.1)
c3 = (0.7,0.7,0.4)
c4 = (4,4,0.7)
c5 = (1.5,1.5,1.3)
c6 = (1,3,0.7)
c7 = (2,3,0.4)
c8 = (3,3,0.9)

print cricle_cluster(c5,c2)
