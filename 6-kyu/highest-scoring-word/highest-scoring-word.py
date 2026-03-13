def high(x):
    a='abcdefghijklmnopqrstuvwxyz'
    di={}
    for i in x.split():
        sum=0
        for j in i:
            if j in a:
                sum+=a.index(j)+1
                di[i]=sum
    maxi=0            
    for i in di:
        if maxi<di[i]:
            maxi=di[i]
    for k in di:
        if di[k]==maxi:
            return k
        
            