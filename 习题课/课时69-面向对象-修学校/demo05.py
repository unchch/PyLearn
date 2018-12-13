class book(object):
    pass

class pen(object):
    pass

def createModel(model):
    info = model()
    return info

obj1 = createModel(book)
obj2 = createModel(pen)

print(obj1, obj2)
print(type(obj1))