def xo(s):
    count_x=0
    count_o=0
    x="xo"
    for i in s.lower():
        if i in x:
            if i=='x':
                count_x+=1
            elif i=='o':
                count_o+=1
            else:
                return True
    return count_x==count_o         
            
            