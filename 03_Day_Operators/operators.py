import math

age = 18
height = 175
complex_number = 1+1j

# Triangle-area
base = float(input("Enter base: "))
height = float(input("Enter hight: "))
print("the area of triangle is", 0.5*base*height)

# Triangle-perimeter
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
print("The perimeter of triangle is", a+b+c)

# Recatngle
length = float(input("Length of rectangle: "))
width = float(input("Width of rectangle: "))
print("Area of rectangle is", length*width)
print("Perimeter of rectangle is", 2*(length+width))

# Circle
radius = float(input("Input radius of circle: "))
print("Area of the circle:", math.pi*radius**2)
print("Circumference of the circle:", 2*math.pi*radius)