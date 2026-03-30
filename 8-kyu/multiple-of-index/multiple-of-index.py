def multiple_of_index(arr):
    ind=[]
    for i in range(len(arr)):
        if i==0:
            if arr[i]==0:
                ind.append(0)
            continue
        if arr[i]%i==0:
            ind.append(arr[i])
    return ind        