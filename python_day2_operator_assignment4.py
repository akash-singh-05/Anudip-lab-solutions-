# Python program to find the area of a triangle whose sides are given

import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"Area of the triangle: {area}")

'''
Ans:-
Enter side a: 4
Enter side b: 6
Enter side c: 7
Area of the triangle: 11.976539567003485 '''
