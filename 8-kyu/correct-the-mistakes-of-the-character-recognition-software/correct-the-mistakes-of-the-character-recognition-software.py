def correct(s):
    res=""
    d={"5":"S","1":"I","0":"O"}
    for i in s:
        if i in d.keys():
            res+=d[i]
        else:
            res+=i
    return res        