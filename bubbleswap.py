# mr park's solution 
def bubble(a_list): 
    swapped = True 
    while swapped: 
        swapped = False
        #the while loop hasn't ended yet
        for i in range(1,len(a_list)):
            if a_list[i-1] > a_list[i]: 
                swapped = True
                a_list[i-1], a_list[i] = a_list[i], a_list[i-1]
        #end for innner for 
    #end of outer for loop
    return a_list 
