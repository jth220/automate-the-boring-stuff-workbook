def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Number can't be 0")
    
    return a/b


print (safe_divide(5, 2))
