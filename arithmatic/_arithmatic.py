# arithmatic.py

def add(x, y):
    try:
        return x + y
    except TypeError:
        raise TypeError('You have different types of data use valid combinations')
        
        
def sub(x, y):
    try:
        return x - y
    except TypeError:
        raise TypeError('You have different types of data use valid combinations')
        
        
def mul(x, y):
    try:
        return x * y
    except TypeError:
        raise TypeError('You have different types of data use valid combinations')
        

def divide(x, y):
    try:
        return x/y
    except TypeError, ZeroDivisionError:
        raise TypeError('You have different types of data use valid combinations or a division by zero')


