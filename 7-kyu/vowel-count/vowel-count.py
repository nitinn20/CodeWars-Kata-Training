def get_count(sentence):
    count=0
    vo="aeiou"
    for i in sentence:
        if i in vo:
            count+=1
    return count        
            
            
        