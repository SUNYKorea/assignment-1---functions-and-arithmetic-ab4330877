# Name: Jungcher An
# SBUID: 115236165
#
# Remove the ellipses (...) when writing your solutions.
# 
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
   
   C = 5/9*(fahrenheit-32)
   return  C

def what_to_wear(C):
    if C >= 20:
        print("T-shirt")
    elif 10 <= C < 20:
        print("Light jacket")
    elif 0 <= C < 10:
        print("Sweater")
    elif -10 <= C < 0:
        print("scarf")
    elif C < -10:
        print("Puffy jacket")
    else:
        print("error")
fahrenheit2celsius(40)
what_to_wear(fahrenheit2celsius(40))
   
# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    
    A = abs(((x1*y2 + x2*y3 + x3*y1) - (x1*y3 + x2*y1 +x3*y2)/2))
    return A

def euclidean_distance(x1, y1, x2, y2):
    
    d = ((x1 - x2)**2 + (y1 - y2)**2)**1/2
    return d

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = ((x1 - x2)**2 + (y1 - y2)**2)**1/2
    s2 = ((x2 - x3)**2 + (y2 - y3)**2)**1/2
    s3 = ((x1 - x3)**2 + (y1 - y3)**2)**1/2
   
    P = s1 + s2 + s3

    
    return P


# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 
import math
def deg2rad(deg):
    K = deg*math.pi/180
    return K
def apothem(number_sides, length_side):
   s = length_side
   n = number_sides
   a = s/2*math.tan(180/n)
   return a

def polygon_area(number_sides, length_side):
   s = length_side
   n = number_sides
   a = s/2*math.tan(180/n)
   A = n*s*a/2
   return A


# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

