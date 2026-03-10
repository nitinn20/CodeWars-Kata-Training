def duplicate_count(text):
    freq={}
    for i in text.lower():
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    count=0        
    for v in freq.values():
        if v>1:
            count+=1
    return count        
     