def persistence(n):
    count=0
    while (n>=10):
        mul=1
        for i in str(n):
            mul*=int(i)
        n=mul    
        count+=1
    return count