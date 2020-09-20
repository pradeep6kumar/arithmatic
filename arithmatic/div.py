def div(x, y):
    try:
        return x/y
    except (TypeError, ZeroDivisionError) as e:
        raise TypeError('You have different types of data use valid combinations or a division by zero')

