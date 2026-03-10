def increment_string(s):
    n = ''
    
    for i in s[::-1]:
        if 48 <= ord(i) <= 57:
            n = i + n
        else:
            break
            
    if n == "":
        return s + "1"
        
    a = s[:len(s) - len(n)]
    next = int(n) + 1
    
    return a + str(next).zfill(len(n))