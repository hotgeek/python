import functools

# 1
value = functools.reduce(lambda x, y: x + y, map(lambda x: x ** 3 + 1, range(1, 51)))
print(value)

# 2
value = functools.reduce(lambda x, y: x * y, map(lambda x : x ** 2 + 1, range(1, 26)))
print(value)

#3
value = functools.reduce(lambda x, y: x+ y, map(lambda x: (x ** 2), range(1, 26))) / 25
print(value)

#4
def seq(n) : return (n+1) / (n ** 2 + 1)
def rms(seq, N):
    return (functools.reduce(lambda x, y: (x + y), map(lambda x : x ** 2, map(seq, range(1, N+1)))) / N) ** 0.5 

#5
value = functools.reduce(lambda x,y: x+y, map(lambda x : (x ** 2) + 1, filter(lambda x: x % 2 == 0 , range(1, 51))))
print(value)

# 6
value = functools.reduce(lambda x,y: x+y, map(lambda x : (x ** 2) + 1, filter(lambda x: x % 2 == 1 , range(1, 51)))) * functools.reduce(lambda x,y: x*y, map(lambda x : (x ** 3), filter(lambda x: x % 2 == 0 , range(1, 26))))
print(value)


