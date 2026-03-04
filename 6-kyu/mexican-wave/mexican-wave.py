def wave(people):
    wave=[]
    for i in range(len(people)):
        res=people[:i]+people[i].upper()+people[i+1:]
        if res!=people:
            wave.append(res)
    return wave    
        
        