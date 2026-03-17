def sort_array(arr):
    odd=[]
    for i in arr:
        if i%2!=0:
            odd.append(i)
    odd.sort()
    count=0
    res=[]
    for i in arr:
        if i%2==0:
            res.append(i)
        else:
            res.append(odd[count])
            count+=1
    return res         
        