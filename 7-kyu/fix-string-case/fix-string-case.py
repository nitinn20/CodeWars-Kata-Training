def solve(s):
    l_c=0
    u_c=0
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            u_c+=1
        elif ord(i)>=97 and ord(i)<=122:
            l_c+=1
    if l_c>=u_c:
        st=s.lower()
    else:
        st=s.upper()
    return st   
            