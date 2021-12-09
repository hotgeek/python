import sys
import traceback
from typing import Type


class NegativeIntegerError(ValueError):
    pass

def factorial(n:int)->int:
    if type(n) != int:
        raise TypeError("Band type for n")

    if n < 0:
        raise NegativeIntegerError("Negative Integer is not allowed")

    rs = 1

    for i in range(1, n+1):
        rs = rs * i
    
    return rs

print("In main")
try:   
   rs = int(input("Enter a number: "))
   factorial(rs)
except TypeError as e:
    print("Sorry I am client, and I am sending wrong type of data:", type(e))
    print("e.args:", e.args)
else:
    print("In else---")
finally:
    print("in Finally")



print("Execution did not terminate")
