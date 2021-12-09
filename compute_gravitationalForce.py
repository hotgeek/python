"""
@autor: Rahul
@goal: Compute the gravitational force given masses and the distance between the masses
"""

str_m1 = input("Enter magnitude of mass object 1:")
m1 = int(str_m1)

str_m2 = input("Enter magnitude of mass object 2:")
m2 = int(str_m2)

str_d = input("Enter distance between 2 masses:")
d = int(str_d)

G = 6.67 * (10  ** -11)

F = (G * m1 * m2)  / (d ** 2)

print("Gravitational force is :", F)

