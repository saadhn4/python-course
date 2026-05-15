# variable scope = where a variable is visible and accesible
# scope resultion = (LEGB) Local -> Enclosed -> Global -> Built-in

from math import e

# def func1():
#     print(x)


# def func2():
#     print(x)


# x = 3

# func1()
# func2()


def func1():
    print(e)


e = 3

# This will print 3 now since e is global
func1()
