def number(lines):
    res=[]
    for i in range(len(lines)):
        res.append(f"{i+1}: {lines[i]}")
    return res    
        