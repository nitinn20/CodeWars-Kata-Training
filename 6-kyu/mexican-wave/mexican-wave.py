def wave(people):
    w=[]
    for i in range(len(people)):
        res=people[:i]+people[i].upper()+people[i+1:]
        if res!=people:
            w.append(res)
    return w        