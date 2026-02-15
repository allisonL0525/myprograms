def expontial(numb, n): 
    if numb == 0:
        return 0 
    elif numb == 1: 
        return 1 
    else: 
        if n == 0: 
            return 1 
        elif n == 1: 
            return numb 
        else: 

def exponent(base, exp): 
    if exp == 0: 
        return 1
    elif exp == 1: 
        return base 
    else: 
        return base * exponent(base, exp-1)
