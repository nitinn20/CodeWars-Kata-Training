def replace_exclamation(st):
    s=''
    v='aeiouAEIOU'
    for i in st:
        if i in v:
            s+='!'
        else:
            s+=i
    return s    