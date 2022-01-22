#Program1
def f():   
    n = 100
    def g():
        print("g:n:", n)    # print 100
    g()   
f()


#Program2
def f():   
    def g():
        print("g:n:", n)    #NameError:
    g()   
    n = 100
f()


#Program3
def f():   
    def g():
        print("g:n:", n)    #Prints 100
    
    n = 100
    g()   
f()