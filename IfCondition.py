"""
@author: Rahul Borkar
@goal: Checking if Condition
"""

str_m1 = input("please enter m1: ")
m1 = int(str_m1)

str_m2 = input("please enter m2: ")
n = int(str_m2)

if(m1 < n) & (m1 < 100):
    print("m1 is less than m2")
    print(" m raise to n is:", m1 ** n)
else:
    print("m1 is greater or equal to m2")
    print(" n raise to m is:", n ** m1)

print("Done")
    
