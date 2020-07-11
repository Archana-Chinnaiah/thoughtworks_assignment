number=input()
root_cube = lambda x: True if int(round(x ** (1. / 3))) ** 3 == x else False
print(root_cube(number))

