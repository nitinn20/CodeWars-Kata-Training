def nb_dig(n, d):
    count=0
    for i in range(n+1):
        sq_str=str(i*i)
        for digit in sq_str:
            if str(d)==digit:
                count+=1
    return count