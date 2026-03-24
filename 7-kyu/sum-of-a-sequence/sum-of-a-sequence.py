def sequence_sum(begin_number, end_number, step):
    sum=0
    l=[]
    for i in range(begin_number,end_number+1,step):
        l.append(i)
    for i in l:
        sum+=i
    return sum    