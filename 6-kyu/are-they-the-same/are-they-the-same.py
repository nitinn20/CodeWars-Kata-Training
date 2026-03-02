def comp(a,b):
    sq=[]
    if a is None or b is None:
        return False
    if len(a)==len(b):
        b.sort()
        for i in a:
            sq.append(i**2)
        sq.sort()
        if b==sq:
            return True
        return False
    else:
        return False
    