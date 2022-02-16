
def logger(decorected_function_obj):
    def inner_function(*args, **kwargs):
        print("This is invoked")
        ret = decorected_function_obj(*args, **kwargs)
        return ret

    return inner_function


def logger1(decorected_function_obj):
    @logger
    def inner_function(*args, **kwargs):
        print("Decorator1 invoked")
        ret = decorected_function_obj(*args, **kwargs)
        return ret

    return inner_function

@logger1
def myfunc(a, b):
    return a+b

print("here it is---:", myfunc(10, 20))