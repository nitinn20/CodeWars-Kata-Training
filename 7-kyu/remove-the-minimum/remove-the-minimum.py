def remove_smallest(numbers):
    if len(numbers)==0:
        return numbers
    n=[]
    for i in numbers:
        n.append(i)
    n.remove(min(n))
    return n