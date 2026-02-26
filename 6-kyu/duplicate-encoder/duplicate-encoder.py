def duplicate_encode(word):
    word=word.lower()
    freq={}
    for i in word:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    new=""
    for i in word:
        if freq[i]==1:
            new+="("
        elif freq[i]>1:   
            new+=")"    
    return new    
        