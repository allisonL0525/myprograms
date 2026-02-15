def selsort(a_list): 
    result = []
    while len(a_list)> 0: 
        val = max(a_list)
        #grabs biggest value in a list 
        #max value is a function is disguse 
        result.append(val)
        a_list.remove(val)
    return 
#simplist one to memorize 


# with bubble sortn

def bubble(a_list): 
    swapped = True 
    while swapped: 
        swapped = False
        for i in range(1,len(a_list)): 
            if a_list[i] > a_list[i-1]: 
                a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
                swapped = True 
    return a_list