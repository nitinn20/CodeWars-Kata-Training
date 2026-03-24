def min_value(digits):
    m=list(set(digits))
    m.sort()
    a=[]
    for i in m:
        a.append(str(i))
    num=("".join(a))
    return int(num)
    