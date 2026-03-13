def points(games):
    count=0    
    for i in games:
        if i[0]>i[2]:
            count+=3
        elif i[0]<i[2]:
            count+=0
        else:
            count+=1
    return count        
                
             