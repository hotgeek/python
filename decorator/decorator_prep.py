# so this hook function will be called as a hook function before my_func is bound to actually built Function object
def my_hook(F):
    print("In my)hook_function")
    print("my_hook_function: type(F):", type(F))
    ret = F()
    print("my_hook_function:ret:", ret)
    return 20 #this will be bount to my_func

@my_hook # Registering a hook function, this causes python to call this hook before binding following body to my_func
def my_func():
    print("-----in my_function----")
    a = 10
    b = 20
    c = a + b
    print(" a:", a, " + b :", b, "= c:", c)
    return c

print("type(my_func)---:", type(my_func))
print("my_func is:", my_func)

"""
execution of header of def statement = compileation of its body 

STEP 1:
compile (a=10) -> machine code1
compile (b=20) -> machine code2
.
.

STEP 2: Prepare Single code object from all seperate Code Objects
code = code1 + code2 + code3

STEP3: Allocate new object of type function and put code object in STEP2 inside it 
FUNCTION->
        code
            -> code1 + code2 + code3

--------------------------HOOK POINT -> only one formal parameter allowed-----------------------------

STEP4: Bind(assign) FUNCTION object in STEP3 with name "my_function"

"""

"""
Output of this program:
In my)hook_function

my_hook_function: type(F): <class 'function'>

"""