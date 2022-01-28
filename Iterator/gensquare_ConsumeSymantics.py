import re


class generate_square:
    def __init__(self, N: int):
        if type(N) != int:
            raise TypeError
        if N < 0 : raise ValueError

        self.N = N
        #For once we are creating a generator
        def get_generator(N):
            for  x in range(1, N+1):
                yield x ** 2

        self.G = get_generator(self.N)

    def __iter__(self):
        return self
    
    def __next__(self):
        return self.G.__next__()      


def main():
    GS = generate_square(5)
    print("First Time ---------------")
    for x in GS:
        print(x)

    # Something like map, following will print empty
    print("Second Time ---------------")
    for x in GS:
        print(x)

main()