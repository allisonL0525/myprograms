def evenodd(a_list): 
    #1 argument --> thus a_list 
    even = []
    #brackets cuz its a empty list; the future you will add stuff in it 
    odd = []
    for val in a_list: 
        if val % 2 == 0: 
            even.append(val)
        else: 
            odd.append(val)
    # end for end 
    if len(even) > len(odd): 
        return even 
    elif len(even) < len(odd): 
        return odd 
    else: 
        return [] 
        #return a empty list --> nothing in here 

        # return a_list.clear() --> return none which we dont want 

time = [1,3,3,6,7,9,9]

print(evenodd(time))