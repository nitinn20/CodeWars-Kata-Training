def disemvowel(string):
    res=""
    vo="aeiouAEIOU"
    for i in string:
        if i not in vo:
            res+=i
    return res        