def inserty(a_list): 
    i = 1 
    while i < len(a_list): 
        j = i 
        while j > 0: 
            if a_list[j-1] > a_list[j]: 
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
            else: 
                break 
            j -= 1 
         i += 1

def arg(list_1,list_2):
    i = 0 
    list_1[i] = list_2[i]
    while i < len(a_list): 
        j = i 
        while j > 0: 
            if a_list[j-1] > a_list[j]: 
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
            else: 
                break 
            j -= 1 
         i += 1
