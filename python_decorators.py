def outer(func):
    def fn():
        print('outer',end="")
        func()
        print('outer',end='')
    return fn


def inner(func):
    def fn():
        print('inner',end='')
        func()
        print('inner',end='')
    return fn


@outer
@inner
def string():
        print("inside",end='')
string()
