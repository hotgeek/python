"""
What shall I do as a resource creator in Python to make it qualify for With statement
"""

import time


class Test:
    def __init__(self):
        print("In Test.__init__")
    
    def __enter__(self):
        print("In Test.__enter__")
        return self # this is why Test() object it bount to t in with statement
    
    def use(self):
        print("Using a resource", end='')
        for _ in range(5):            
            print(".", end='', flush=True)
            time.sleep(1)
        print()

    def __exit__(self, p1, p2, p3):
        print("In Test.__exit__")
        return True

def main():
    print("About to enter 'with' Block")
    with Test() as t:
        t.use()
    print("Out of 'with' block")

main()