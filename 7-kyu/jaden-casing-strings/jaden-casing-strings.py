def to_jaden_case(string):
    res=[]
    for i in string.split():
        res.append(i.capitalize())
    result=" ".join(res)
    return result
        
        