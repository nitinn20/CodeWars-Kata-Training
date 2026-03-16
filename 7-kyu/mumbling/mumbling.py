def accum(st):
    s=[]
    for i in range(len(st)):
        s.append(st[i].lower()*(i+1))
    p=[] 
    for i in s:
        p.append(i[0].upper()+i[1:])
    return ("-".join(p))    
   
        