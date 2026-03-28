def bin_to_decimal(inp):
    if inp=='0':
        return 0
    sum=0
    input=inp[::-1]
    for i in range(len(input)):
        if input[i]=='1':
            sum+=2**i
    return sum    