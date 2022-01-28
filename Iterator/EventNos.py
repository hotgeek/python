class EvenNos_Iterator:
    def __init__(self, G):
        self.G = G

    def __next__(self):
        return self.G.__next__()

class EvenNos:
    def __init__(self, L):
        if(type(L) != list):
            raise TypeError
        
        for x in L:
            if(type(x) != int):
                raise TypeError

        self.L = L

    def __iter__(self):
        def get_generator(lst):
            for x in lst:
                if x % 2 == 0:
                    yield x
        G = get_generator(self.L)
        EI = EvenNos_Iterator(G)
        return EI

def main():
    L = [1, 2, 3, 4,5,6,7,8,9,10]
    test = EvenNos(L)
    for x in test:
        print(x)

main()
