"""
@author: Rahul
@goal: To Compute the distance between 2 points whose coordinates are given"
"""

str_x1 = input("Enter X-Coodinate of Point 1: ")
x1 = float(str_x1)

str_y1 = input("Enter Y-Coodinate of Point 1: ")
y1 = float(str_y1)

str_x2 = input("Enter X-Coodinate of Point 2: ")
x2 = float(str_x2)

str_y2 = input("Enter Y-Coodinate of Point 2: ")
y2 = float(str_y2)


# Square root is 1/2, cube root is 1/3
d = ((y2 - y1) ** 2 + (x2 - x1) ** 2)** 0.5
print("Distance: ", d);
