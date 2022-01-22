from tkinter.messagebox import NO


class FunctionWrapper:
    def __init__(self, function_object):
        if(type(function_object) != type(lambda: None)):
            raise TypeError
        
        self.function_object = function_object

    def __call__(self,  *args, **kwargs):
        return self.function_object(*args, **kwargs)


def compute_1(a, b):
    return a + b

def compute_2(x, y, *a, z = 100, w=200, p, q):
    print(x, y)
    print(a)
    print(z, w)
    print(p, q)
    return x**2 + y**2

def main():
    wp1 = FunctionWrapper(compute_1)
    wp2 = FunctionWrapper(compute_2)

    print(wp1(10, 5))
    print(wp2(10, 5, 100, 200, 300, w= -200, p = 'abc', q="sas"))

main()

    
