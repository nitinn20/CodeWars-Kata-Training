def calculate_years(principal, interest, tax, desired):
    d=0
    years=0
    p0=principal
    if principal==desired:
        return 0
    else:
        while(d<desired):
            inter=p0*interest
            taxi=inter*tax
            d=p0+inter-taxi
            years+=1
            p0+=inter-taxi
        return years     
        
        
        
        
​
    
​