def accum(st):
    res = []
    for i in range(len(st)):
        res.append(st[i].lower()*(i+1)) 
    p = []
    for i in res:
        p.append(i[0].upper()+i[1:])
    return ("-".join(p))
    
    