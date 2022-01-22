import sys

def cartesian_product():
    L = [x**2 - y**3 + z** 4 for x in range(1, 10) if x % 2 == 0
                             for y in range(5, 15) if y % 3 == 2
                             for z in range(3, 8) if z % 2 == 1
                             if ( x**2 - y**3 + z**4) > 0 
        ]
    print(L)

cartesian_product()
