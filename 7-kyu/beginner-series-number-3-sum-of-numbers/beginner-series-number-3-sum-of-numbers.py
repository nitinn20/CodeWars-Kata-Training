def get_sum(a,b):
    sum=0
    start=min(a,b)
    end=max(a,b)
    for i in range(start,end+1):
        sum+=i
    return sum    
        