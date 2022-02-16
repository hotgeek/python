# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

a1 = np.zeros(8)
print("Dimentions:", a1.ndim)
print("Shape:", a1.shape)

for i in range (a1.shape[0]):
    a1[i] = (i+1) * 10
    
print("a1:", a1)

a2 = a1 + 10

print("a2:", a2)

a3 = a2 - 5
print("a3:", a3)

a4 = a3 * 8
print("a4:", a4)

a5 = a4 // 2
print("a5:", a5)

#------------------------------------------

a1 = np.zeros(8)
a2 = np.zeros(8)

for i in range(a1.shape[0]):
    a1[i] = (i+1) *10
    a2[i] = (i+1) * 5
    
print(a1)
print(a2)

a3 = a1 + a2
print("a3:", a3)

a4 = a1 * a2
print("a4:", a4)

a5 = a1 - a2
print("a5:", a5)

a6 = a1 // a2
print("a6:", a6)

a7 = a1 ** a2
print("a7:", a7)

"""
array1 * array2

for element in array:
    element * constant 

for i in range(array1.shape[0]):
    array1[i] * array2[i]
"""

m1 = np.identity(3)
m2 = np.identity(3)

print("M1:", m1)
print("M2", m2)

m3 = m1 + m2
print("M3:", m3)

#--------------------------------
# Transpose

a1= np.arange(15)
print(a1)
print("a1.ndim={} a1.shape={}".format(a1.ndim, a1.shape))

a2 = a1.reshape(3, 5)
print(a2)
print("a2.ndim={} a2.shape={}".format(a2.ndim, a2.shape))

a3 = a1.reshape(5, 3)
print(a3)
print("a3.ndim={} a3.shape={}".format(a3.ndim, a3.shape))

a1 = np.arange(12)
a2 = a1.reshape(2, 6)
a3 = a1.reshape(6, 2)
a4 = a1.reshape(3, 4)
a5 = a1.reshape(4, 3)
a6 = a1.reshape(3,2,2)
a7 = a1.reshape(2, 3, 2)

def print_dim_shape(a):
    print("a.dim= {} a.shape = {}".format(a.ndim, a.shape))
    print(a)
    
for a in (a1, a2, a3, a4, a5, a6, a7):
    print_dim_shape(a)
    
#------------------------------------
a1 = np.arange(12)
a2 = a1.reshape((2, 6))

print_dim_shape(a2)

a3 = a2.T
print_dim_shape(a3)

#-----------------------------------------
#ufuncs

a1 = np.arange(8)
a2 = np.sqrt(a1)

print("a1:", a1, "\na2 : ", a2)

a3 = np.floor(a2)
print("a3:", a3)

# exploration of unary ufuncs 
# a + ib = sqrt(a**2+b**2)

a = np.array([n**2 - 10 for n in range(-5, 5)])
print("a :", a)

a1 = np.abs(a)
print("a1:", a1)

c1 = complex(1.1, 2.2)
print(c1)


