

#L = [x ** 2 for x in range(1,11) if x % 2 == 0]

L1 = list(range(1, 11))
fL1 = []
for x in L1:
    if(x % 2 == 0):
        fL1.append(x ** 2)

print(fL1)

L2 = list(map(lambda n : n ** 2, filter(lambda n : n % 2 == 0, range(1, 11))))
print(L2)

filter 

