def name_shuffler(s):
    res=[]
    for i in s.split():
        res.append(i)
    res.reverse()    
    return (' '.join(res))    
        
        
        