def dig_pow(n, p):
    pcount=p
    res=0
    for i in str(n):
        res+=int(i)**pcount
        pcount+=1
    k=res/n
    if k.is_integer():
        return k
    return -1
        
        