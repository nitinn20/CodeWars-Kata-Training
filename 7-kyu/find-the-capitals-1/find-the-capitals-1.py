def capitals(word):
    ind=[]
    for i in range(len(word)):
        if ord(word[i])>=65 and ord(word[i])<=90:
            ind.append(i)
    return ind        
            