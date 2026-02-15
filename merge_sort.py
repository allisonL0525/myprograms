def mergeSort(a_list): 
    #consider as the splitter
    
    #  Base Case 
    if len(a_list) <= 1: 
        return a_list 
    # word towards base case 
   
    mid = len(a_list) // 2
    first_half = a_list[:mid]
    second_half = a_list[mid:]
    # seperated the 2 parts into 2 equal parts 
   
    first_half = mergeSort(first_half) # RESURSIVE CALL :O
    second_half = mergeSort(second_half)# ANOTHER RECUSRSIVE CALL
    # calls itself 

    return combine(first_half,second_half)




def combine(left,right): 
    #assumes that left and right are sorted 
    if len(left) == 0 and len(right) == 0:
        return []
    elif len(left) == 0: 
        return right 
    elif len(right) == 0: 
        return left
    # base cases when left and right are empty --> some cases where 1 is empty 
    else: 
        # when both left and right has value 
        i = 0 # for left, very left of left 
        j = 0 # for right, very right og right 
        answer = [] #shove the sorted stuff here 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                answer.append(left[i])
                i +=1 
            else: 
                answer.append(right[i])
                j += 1 
    #what if we have values left over 
    while i < len(left): 
        answer.append(left[i])
        i+= 1 
    while j < len(right): 
        answer.append(right[j])
        j += 1 
    return answer

                    
    
