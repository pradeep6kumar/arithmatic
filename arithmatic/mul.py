     
def mul(x, y):
    try:
        return x * y
    except TypeError:
        raise TypeError('You have different types of data use valid combinations')
