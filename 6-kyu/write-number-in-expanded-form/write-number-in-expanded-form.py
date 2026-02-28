def expanded_form(num):
    s=str(num)
    s=s[::-1]
    parts=[]
    for i in range(len(s)):
        value=(int(s[i])*(10**i))
        if value!=0:
            parts.append(str(value))
    parts.reverse()
    return (" + ".join(parts))
​
        
        
                
    