

L1 = list(range(1,10))
fL1 = []
for x in L1:
    if x % 2 == 0:
        fL1.append(x)
    
#function for filtered iter1
for i in range(len(fL1)):
    fL1[i] = fL1[i] ** 2

L2 = list(range(5,15))
fL2 = []
for x in L2:
    if x % 3 == 2:
        fL2.append(x)

for i in range (len(fL2)):
    fL2[i] = fL2[i] ** 3


L3 = list(range(3, 8))
fL3 = [] 
for x in L3:
    if x % 2 == 1:
        fL3.append(x)

for i in range(len(fL3)):
    fL3[i] = fL3[i] ** 4

#Cartesion Product
cart = []
for x in fL1:
    for y in fL2:
        for z in fL3:
            T = (x, y, z)
            cart.append(T)

# apply function g
rs1 = []
for t in cart:
    rs1.append(t[0] - t[1] + t[2])

#apply  filter on rs1
rs = []
for x in rs1:
    if x > 0:
        rs.append(x)

del L1, L2, L3, fL1, fL2, fL3, cart, rs1

print(rs)


