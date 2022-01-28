"""
IF there are exception inbetweeb the resource is not released 
"""

class T:
    def __init__(self, init_data):
        #construct self
        pass

    def __enter__(self):
        ## Post initialization of construction of self
        pass

    def use1(self):
        pass

    def use2(self):
        pass

    def __exit__(self, p1, p2, p3):
        print("in exit- releasing resource")
    
    def raiseTypeError():
        raise TypeError

def main():
    with T() as t:
        t.use1()
        # unhandled exception 
    