def f1():
    a = 10
    b = 20
    c = a + b  
    def f2():
        p = 'xyz'
        q = 'lmn'

        r = p + q

        def f3():
            u = 1.1
            v = 2.2
            w = u + v            
            print("f3.locals():", locals())
        
        f3()
    
        print("f2.locals():", locals())
    f2()
    print("f1.locals", locals())
f1()
print("globals()->", globals())

"""
How many symbol tables are present in Python Program 
1. Modulewide Symbol table -> global symbol table
    can be printed with function calls to globals()
2. Every new function and class will have its own symbol table!
"""