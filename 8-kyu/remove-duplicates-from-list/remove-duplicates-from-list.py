def distinct(seq):
    dit={}
    res=[]
    for i in seq:
        if i in dit:
            dit[i]+=1
        else:
            dit[i]=1
            res.append(i)
    return res        