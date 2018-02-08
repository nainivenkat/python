import math
'''
Method to identify overlapping circles from the two input circles provided as input 
'''
def overlap(circle1, circle2):
    x1,y1,r1 = circle1
    x2,y2,r2 = circle2
    width = abs(x1-x2)
    height = abs(y1-y2)
    tuplex = tuple((0,0,0))
    distance = math.sqrt(width**2 + height**2)

    if distance <= (r1 + r2):
        return circle1, circle2
    return 0
'''
Method to calculate area of circle to determine biggest circle in overlapping circles
'''
def area_circle(circle):
    x1,y1,r1 = circle1
    area = math.pi*r1**2
    return area

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
    overlap_circles = []
    nonoverlap_circles = []
    output_circles = []

    # Since the input arguments can be any number, *args let us provide dynamic input. Function populates circles list
    for circle in args:
        circles.append(circle)

    #going over the loop and checking each circle with over to find the overlapping circles
    for i in range(len(circles)):
        for j in range(i+1, len(circles)):
            overlap_circle = overlap(circles[i],circles[j])
            if overlap_circle:
                for element in overlap_circle:
                    overlap_circles.append(element)

    # remove overlapping circles from the circles list, gives non-overlap circle list
    for element in circles:
        if element not in overlap_circles:
            nonoverlap_circles.append(element)

    #Following code will give the list of overlapping circles with the biggest circle as first element
    overlap_circles = list(set(overlap_circles))
    overlap_circles = sorted(overlap_circles, key = getkey, reverse=True)
 

    if overlap_circles and nonoverlap_circles:
        output_circles = [(element) for element in nonoverlap_circles]
        output_circles.append(overlap_circles[0])
        output_circles.sort()
        return output_circles
    elif nonoverlap_circles:
        output_circles = [(element) for element in nonoverlap_circles]
        return  output_circles
    else:
        output_circles.append(overlap_circles[0])
        return output_circles


c1 = (0.5,0.5,0.5)
c2 = (1.5,1.5,1.1)
c3 = (0.7,0.7,0.4)
c4 = (4,4,0.7)
c5 = (1.5,1.5,1.3)
c6 = (1,3,0.7)
c7 = (2,3,0.4)
c8 = (3,3,0.9)

#First condition
print cricle_cluster(c1,c2,c3,c4)

#second condition
print cricle_cluster(c5,c4)

#Third condition
print cricle_cluster(c6,c7,c8)

#Final condition where all the circles put together
#print cricle_cluster(c1,c2,c3,c4,c5,c6,c7,c8)
