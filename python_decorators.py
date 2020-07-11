def outer(func):
    def fn():
        print('outer')
        func()
        print('outer')
    return fn


def inner(func):
    def fn():
        print('inner')
        func()
        print('inner')
    return fn


@outer
@inner
def string():
        print("inside")
string()
