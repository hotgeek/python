import sys
import time
import traceback
def logger(logged_function_object):
    def inner_function(*args, **kwargs):
        try:
            log_handle = open("log.txt", "a")
        except FileNotFoundError:
            print("Invalid Path for file")
            sys.exit(-1)
        except PermissionError:
            print("No sufficient file permissions")
            sys.exit(-1)

        line = '-' * 70
        print(line, logged_function_object.__name__, file=log_handle)
        print("Time of call:", time.ctime(time.time()), file=log_handle)
        print("Arguments:", file=log_handle)
        if len(args) != 0:
            print("Non keyword Arguments:", file=log_handle)
            for i in range(len(args)):
                print("args[{}]:{}, type(args[{}]:{}".format(i, args[i], i, type(args[i])), file=log_handle)

        if len(kwargs) != 0:
            print("Keyword Arguments:", file=log_handle)
            for i in range(len(args)):
                print("args[{}]:{}, type(args[{}]:{}".format(i, kwargs[i], i, type(kwargs[i])), file=log_handle)

        try:
            ret = logged_function_object(*args, **kwargs)
        except:
            exc_name, exc_data, exc_tb = sys.exc_info()
            print(exc_name, exc_data, sep=":", file=log_handle)
            traceback.print_tb(exc_tb, file=log_handle)
            log_handle.close()
            sys.exit(-1)

        print("ret={}, type(ret)={}".format(ret, type(ret)))
        log_handle.close()
        return ret

    return inner_function

@logger
def my_func(a, b):
    print("called my_func---", a+b)
    return a+b

my_func(10, 20)

