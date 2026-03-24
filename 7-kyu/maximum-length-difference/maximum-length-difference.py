def mxdiflg(a1, a2):
    if len(a1)==0 or len(a2)==0:
        return -1
    x=[]
    for i in a1:
        x.append(len(i))
    y=[] 
    for i in a2:
        y.append(len(i)) 
​
    diff1=abs(max(x)-min(y))
    diff2=abs(min(x)-max(y))
    return max(diff1,diff2) 
     
    