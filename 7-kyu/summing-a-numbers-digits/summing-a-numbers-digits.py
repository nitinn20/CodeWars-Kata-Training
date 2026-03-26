def sum_digits(number):
    n=abs(number)
    sum=0
    while(n>0):
        rem=n%10
        sum+=rem
        n=n//10
    return sum    