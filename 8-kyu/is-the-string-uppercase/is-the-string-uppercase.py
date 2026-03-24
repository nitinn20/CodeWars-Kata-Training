def is_uppercase(inp):
    for i in inp:
        if ord(i)>=97 and ord(i)<=122:
            return False
    return True