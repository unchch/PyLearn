# gloabls locals

a = 1
b = 2


def fun(c, d):
    e = 111
    print("Local={0}".format(locals()))
    print("Globals={0}".format(globals()))


fun(100, 200)