def wave(s):
    l=[]
    for i in range(len(s)):
        res = ''
        res = s[:i]+ s[i].upper() + s[i+1:]
        if s != res:
            l.append(res)
    return l