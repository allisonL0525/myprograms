def numvslet(a): 
    i = 0 
    letter = 0 
    number = 0 
    while len(a) > 0: 
        if item is a.alpha(): 
            letter += 1
        elif item is a.isdigit(): 
            number += 1 
    if letter > number:  
        return 1 
    elif letter < number: 
        return -1 
    else: 
        return 0 

def numvslet(a): 
    letter_count = 0 
    number_count = 0 
    for char in a: 
        if char.isalpha(): 
            letter_count += 1
        elif char.isdigit(): 
            number_count += 1 
    if letter_count > number_count:   
        return 1 
    elif letter_count < number_count: 
        return -1 
    else: 
        return 0