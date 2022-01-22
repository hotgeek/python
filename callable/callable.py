class Test:
    def __call__(self):
        print("In Test.__call__")
        print("Test.__call__:type(self):{}, id(self): {}".format(type(self), id(self)))

def main():
    t = Test()
    print("main: type():{} id(t): {}".format(type(t), id(t)))
    t()

main()