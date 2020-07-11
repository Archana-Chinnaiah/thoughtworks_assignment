'''1.debug to get output: hello
                          hello
'''
def function_outside():
    msg="Hi"
    def function_inside():
       nonlocal msg
       msg="Hello"
       print(msg)
    function_inside()
    print(msg)
function_outside()
print()



'''2.Debug the program to get output : 1
and also briefly explain the reason why ?
'''
def f(x):
    def g(y=x):
        return y
    return g
a=5
b=1
h=f(b)
print(h())

REASON:
# we need to change f(a)->f(b) to get the output as 1
#we pass arguments to object 'h' so h(b)->h()

