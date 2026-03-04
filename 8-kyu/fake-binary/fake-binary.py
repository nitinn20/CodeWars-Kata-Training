def fake_bin(x):
    res=""
    for digit in x:
        if int(digit)>=5:
            res+='1'
        else:
            res+='0'
    return res         