def is_square(n):  
    if n<0:
        return False
    sqrt=n**0.5
    if sqrt%1==0:
        return True
    return False
    