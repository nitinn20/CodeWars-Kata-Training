def tribonacci(signature, n):
    if n==0:
        return []
    elif n<3:
        return signature[0:n]
    a=signature[0]
    b=signature[1]
    c=signature[2]
    for i in range(3,n):
        next=a+b+c
        signature.append(next)
        a=b
        b=c
        c=next
    return signature   
        
        