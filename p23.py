# def missing(a_list): 
#     largest = max(a_list)
#     if len(a_list) == 0: 
#         return 0 
#     elif: 
#         if 
#     else: 
#         return a_list[largest]  
        

def missing(array): 
    limit = len(array)
    freq_table = {}
    for x in array: 
        freq_table[x] = 1 
    
    for i in range(0,limit+1): 
        if i not in freq_table: 
            return i 
    return -1 
    
#better way to do than the function above 
    # no longer a linear serach 
for i in range(0,limit+1): 
    if i not in array: 
        return i 



# scrabble 

def scrabble(word): 
    score = {}
    score