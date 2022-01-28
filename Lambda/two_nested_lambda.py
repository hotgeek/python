
value = (lambda n : lambda x : x ** n)(2)(2)
print("Double lambda---", value)


value = (lambda a, b, c = 10: a + b + c)(2, 4)
print("Complex lambda---", value)

value = (lambda *args: print(args, type(args)))('a', 1, 2.45)

(lambda a, b, c, *args, d=100, e=200, f, g, **kwargs: 
    print(a,b,c,args,d,e,f,g,kwargs))(10, 20, 40, 50, 60, e=-300, f="hello", g ='f', m=10, n=20, q=30)



