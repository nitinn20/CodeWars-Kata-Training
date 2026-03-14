def gimme(input_array):
    res=input_array.copy()
    res.sort()
    mid=res[1]
    return input_array.index(mid)