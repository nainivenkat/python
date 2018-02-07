import math
'''
Method to identify overlapping circles from the two input circles provided as input 
'''
def overlap(circle1, circle2):
    x1,y1,r1 = circle1
    x2,y2,r2 = circle2
    base = abs(x1-x2)
    height = abs(y1-y2)
    distance = math.sqrt(base**2 + height**2)

    if distance <= (r1 + r2):
        if r1 < r2:
            return circle1
        else:
            return circle2
    return (0,0,0)

'''
Method to take list of arguments as circles and remove overlapping circles. 
'''
def cricle_cluster(*args):
    circles = []
    remove_circles = []
    large_circles = []

    # Since the input arguments can be any number, *args let us provide dynamic input. Function populates circles list
    for circle in args:
        circles.append(circle)

    #going over the loop to checking each circle with over to find the overlapping circles
    for i in range(len(circles)):
        for j in range(i+1, len(circles)):
            remove_circle = overlap(circles[i],circles[j])
            if remove_circle:
                remove_circles.append(remove_circle)

    # remove overlapping circles from the circles list, gives non-overlap circle list
    for element in circles:
        if element in remove_circles:
            circles.remove(element)
    return circles

 
'''
c1 = (0.5,0.5,0.5)
c2 = (1.5,1.5,1.1)
c3 = (0.7,0.7,0.4)
c4 = (4,4,0.7)
'''
'''
c1 = (1.5,1.5,1.3)
c2 = (4,4,.07)
'''
'''
c1 = (1,3,0.7)
c2 = (2,3,0.4)
c3 = (3,3,0.9)
'''
c1 = (1,3,0.7)
c2 = (2,3,0.4)
c3 = (3,3,0.9)

print cricle_cluster(c1,c2,c3)
