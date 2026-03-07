def alphabet_position(text):
    result=[]
    for i in text.lower():
        if i.isalpha():
            result.append(str(ord(i)-ord('a')+1))
    return (" ".join(result))        