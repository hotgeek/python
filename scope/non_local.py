def f():
    n = 100

    def g():
        nonlocal n
        n = "Hello"
        print("g():n:", n)

    print("f():n", n)
    g()
    print("f():n", n)

f()