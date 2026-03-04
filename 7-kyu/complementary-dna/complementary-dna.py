def DNA_strand(dna):
    res=""
    for char in dna:
        if char=='A':
            res+='T'
        elif char=='T':
            res+='A'
        elif char=='C':
            res+='G'
        elif char=='G':
            res+='C'
        else:
            res+=char
    return res    
    