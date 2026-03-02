def str_count(strng, letter):
    freq={}
    for i in strng:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in freq:
        if letter==i:
            return freq[i]
    return 0